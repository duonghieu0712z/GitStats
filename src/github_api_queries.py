#!/usr/bin/python3

from aiohttp.client_exceptions import ClientPayloadError
from requests import post, get, models
from asyncio import Semaphore, sleep
from aiohttp import ClientSession
from http import HTTPStatus
from typing import Optional
from json import loads


###############################################################################
# GitHubApiQueries class
###############################################################################


class GitHubApiQueries(object):
    """
    Class with functions to query the GitHub GraphQL (v4) API and the REST (v3)
    API. Also includes functions to dynamically generate GraphQL queries.
    """

    __GITHUB_API_URL: str = "https://api.github.com/"
    __GRAPHQL_PATH: str = "graphql"
    __REST_QUERY_LIMIT: int = 10
    __ASYNCIO_SLEEP_TIME: int = 5
    __DEFAULT_MAX_CONNECTIONS: int = 10

    def __init__(
        self,
        username: str,
        access_token: str,
        session: ClientSession,
        max_connections: int = __DEFAULT_MAX_CONNECTIONS,
    ) -> None:
        self.username: str = username
        self.access_token: str = access_token
        self.session: ClientSession = session
        self.semaphore: Semaphore = Semaphore(max_connections)
        self.headers: dict[str, str] = {
            "Authorization": f"Bearer {self.access_token}",
        }

    async def query(self, generated_query: str) -> dict[str, dict]:
        """
        Make a request to the GraphQL API using the authentication token from
        the environment
        :param generated_query: string query to be sent to the API
        :return: decoded GraphQL JSON output
        """
        try:
            async with self.semaphore:
                r_async = await self.session.post(
                    url=self.__GITHUB_API_URL + self.__GRAPHQL_PATH,
                    headers=self.headers,
                    json={"query": generated_query},
                )
            result: dict[str, dict] = await r_async.json()

            if result is not None:
                return result
        except (ConnectionError, ClientPayloadError) as err:
            print("aiohttp failed for GraphQL query. Msg:", str(err))

            # Fall back on non-async requests
            async with self.semaphore:
                r_requests = post(
                    url=self.__GITHUB_API_URL + self.__GRAPHQL_PATH,
                    headers=self.headers,
                    json={"query": generated_query},
                )
                result = r_requests.json()

                if result is not None:
                    return result
        return dict()

    async def query_rest(
        self, path: str, params: Optional[dict] = None
    ) -> dict[str, str | int | dict | list[dict[str, str]]] | list[dict[str, any]]:
        """
        Make a request to the REST API
        :param path: API path to query
        :param params: Query parameters to be passed to the API
        :return: deserialized REST JSON output
        """
        for i in range(self.__REST_QUERY_LIMIT):
            if params is None:
                params = dict()
            if path.startswith("/"):
                path = path[1:]

            try:
                async with self.semaphore:
                    r_async = await self.session.get(
                        self.__GITHUB_API_URL + path,
                        headers=self.headers,
                        params=tuple(params.items()),
                    )

                if r_async.status == HTTPStatus.ACCEPTED.value:
                    print(f"A path returned {HTTPStatus.ACCEPTED.value}. Retrying...")
                    await sleep(self.__ASYNCIO_SLEEP_TIME)
                    continue

                result: dict[str, str | dict] = await r_async.json()

                if result is not None:
                    return result
            except (ConnectionError, ClientPayloadError) as err:
                print(
                    "aiohttp failed for REST query attempt #" + str(i + 1),
                    " msg:",
                    str(err),
                )

                # Fall back on non-async requests
                async with self.semaphore:
                    r_requests = get(
                        self.__GITHUB_API_URL + path,
                        headers=self.headers,
                        params=tuple(params.items()),
                    )

                    if r_requests.status_code == HTTPStatus.ACCEPTED.value:
                        print(
                            f"A path returned {HTTPStatus.ACCEPTED.value}. Retrying..."
                        )
                        await sleep(self.__ASYNCIO_SLEEP_TIME)
                        continue
                    elif r_requests.status_code == HTTPStatus.OK.value:
                        return r_requests.json()

        print(
            f"Too many {HTTPStatus.ACCEPTED.value}s. Data for this repository will be incomplete."
        )
        return dict()

    @staticmethod
    def get_user() -> str:
        """
        :return: GraphQL query with user login and name
        """
        return """
            {
                viewer {
                    login
                    name
                }
            }"""

    @staticmethod
    def repos_overview(
        contrib_cursor: Optional[str] = None, owned_cursor: Optional[str] = None
    ) -> str:
        """
        :return: GraphQL queries with overview of user repositories
        """
        return f"""
            {{
                viewer {{
                    login,
                    repositories(
                    first: 100,
                    orderBy: {{
                        field: UPDATED_AT,
                        direction: DESC
                    }},
                    after: {
        'null' if owned_cursor is None
        else """ + owned_cursor + """
        }) {{
                        pageInfo {{
                            hasNextPage
                            endCursor
                        }}
                        nodes {{
                            nameWithOwner
                            stargazers {{
                                totalCount
                            }}
                            forkCount
                            isFork
                            isEmpty
                            isArchived
                            isPrivate
                            languages(first: 20, orderBy: {{
                                field: SIZE,
                                direction: DESC
                            }}) {{
                                edges {{
                                    size
                                    node {{
                                        name
                                        color
                                    }}
                                }}
                            }}
                        }}
                    }}
                    repositoriesContributedTo(
                    first: 100,
                    includeUserRepositories: false,
                    orderBy: {{
                        field: UPDATED_AT,
                        direction: DESC
                    }},
                    contributionTypes: [
                        COMMIT,
                        PULL_REQUEST,
                        REPOSITORY,
                        PULL_REQUEST_REVIEW
                    ]
                    after: {
        'null' if contrib_cursor is None
        else """ + contrib_cursor + """}) {{
                        pageInfo {{
                            hasNextPage
                            endCursor
                        }}
                        nodes {{
                            nameWithOwner
                            stargazers {{
                                totalCount
                            }}
                            forkCount
                            isFork
                            isEmpty
                            isArchived
                            isPrivate
                            languages(first: 20, orderBy: {{
                                field: SIZE,
                                direction: DESC
                            }}) {{
                                edges {{
                                    size
                                    node {{
                                        name
                                        color
                                    }}
                                }}
                            }}
                        }}
                    }}
                }}
            }}"""

    @staticmethod
    def contributions_all_years() -> str:
        """
        :return: GraphQL query to get all years the user has been a contributor
        """
        return """
            query {
                viewer {
                    contributionsCollection {
                        contributionYears
                    }
                }
            }"""

    @staticmethod
    def contributions_by_year(year: str) -> str:
        """
        :param year: year to query for
        :return: portion of a GraphQL query with desired info for a given year
        """
        return f"""
            year{year}: contributionsCollection(
            from: "{year}-01-01T00:00:00Z",
            to: "{int(year) + 1}-01-01T00:00:00Z"
            ) {{
                contributionCalendar {{
                    totalContributions
                }}
            }}"""

    @classmethod
    def all_contributions(cls, years: list[str]) -> str:
        """
        :param years: list of years to get contributions for
        :return: query to retrieve contribution information for all user years
        """
        by_years: str = "\n".join(map(cls.contributions_by_year, years))
        return f"""
            query {{
                viewer {{
                    {by_years}
                }}
            }}"""

    @staticmethod
    def get_language_colors() -> dict[str, dict[str, str]]:
        url: models.Response = get(
            "https://raw.githubusercontent.com/ozh/github-colors/master/colors.json"
        )
        return loads(url.text)

# 📈 [GitHub Stats Visualization](https://github.com/R055A/GitStats) 🔭

Generate regularly updated visualizations of user and repository statistics from the GitHub [GraphQL](https://docs.github.com/en/graphql) and [REST](https://docs.github.com/en/rest) APIs using GitHub [Actions](https://docs.github.com/en/actions) and [Secrets](https://docs.github.com/en/actions/security-guides/encrypted-secrets). Customizable visualizations support dark and light mode and can adapt to device sizes.

> A modification of [`jstrieb/github-stats`](https://github.com/jstrieb/github-stats) visualizations with new and improved statistics and more options!

[![GitStats Overview](https://raw.githubusercontent.com/R055A/GitStats/actions_branch/generated_images/overview.svg)![GitStats Languages](https://raw.githubusercontent.com/R055A/GitStats/actions_branch/generated_images/languages.svg)](https://github.com/R055A/GitStats)

> _Note: my '**Avg contributions**' stats is customized to only consider collaborative [university project repos](https://github.com/University-Project-Repos)_

## Description of Statistical Terminology

| GitHub Statistics Term         | Description                                                                                                    |
|--------------------------------|----------------------------------------------------------------------------------------------------------------|
| All-time GitHub contributions  | Count of all contributions ([as defined by GitHub](https://docs.github.com/en/account-and-profile/setting-up-and-managing-your-github-profile/managing-contribution-settings-on-your-profile/viewing-contributions-on-your-profile)) to any and all repositories any time for a given user |
| Lines of code changes*         | Sum of all code additions and deletions to all repositories contributed to for a user, measured by lines       |
| Avg contributions [weighted]*  | Average code changes per collaborative repository for a user [weighted relative to contributor count]          |
| Repos contributed [% collab]*  | Count of all repositories contributed to by a user [including percent in collaboration with others]            |
| Repo views (as of YYYY-MM-DD)* | Sum of views to all repositories since created, if owned, or contributed to (from a given date)                | 
| Repo collaborators*            | Sum of collaborator and contributor counts for all repositories contributed to or owned for a user             |
| Repo forks*                    | Sum of all-time fork counts for all repositories contributed to or owned for a user                            |
| Repo stars*                    | Sum of all-time star counts for all repositories contributed to or owned for a user                            |
| # [+#] Implemented Languages*  | Listed [and hidden] percentages of implemented languages relative to sizes of files contributed to             |

> \* Customisable as instructed in the :closed_lock_with_key: Options section below

# :rocket: Instructions

<details>
<summary>Click drop-down to view step-by-step instructions for generating your own GitHub statistics visualizations
</summary>

### Copy Repository

1. Click either link to start generating your own GitHub statistic visualizations: 
   1. [Generate your own copy of this repository without the commit history](https://github.com/R055A/GitStats/generate)
      * *Note: the first GitHub Actions workflow initiated at creation of the copied repository is expected to fail*
   2. [Fork a copy of this repository with the commit history configured to sync changes](https://github.com/R055A/GitStats/fork)
      * *Note: this copies all branches including the `action_branch` with statistics, but this can be overwritten*

### Generate a New Personal Access Token

2. Generate a personal access token by following these steps:
   1. If you are logged in, click this link to: [generate a new "classic" token](https://github.com/settings/tokens/new)
      * *Otherwise, to learn how to generate a personal access token: [read these instructions](https://docs.github.com/en/github/authenticating-to-github/creating-a-personal-access-token)*
   2. Ensure it is a "classic" token being generated and not a "fine-grained" token
   2. Name the token
   3. Select your preferred '***Expiration***' date
   4. Select `repo` for '<u>**Full control of private repositories**</u>'
   5. Select `read:user` to '<u>**Read only ALL user profile data**</u>'
   6. Click the '***Generate token***' button
   7. Copy the generated token - there is only one opportunity provided for this

### Create ACCESS_TOKEN Secret

3. Create a repository secret for the personal access token by following these steps:
   1. If this is your copy of the repository, click this link to: [create a new secret](../../settings/secrets/actions/new)
      * *Otherwise, go to repository **Settings**, click the **Secrets** option, then click **New repository secret***
   2. Name the new secret: `ACCESS_TOKEN`
   3. Enter the generated **[personal access token](#generate-a-new-personal-access-token)** as the '*Value*'

### Run GitHub Actions Workflow

4. Manually generate GitHub statistics visualizations:
   1. This can be done using any of the following two GitHub Actions workflows:
      1. For the **first time**, or to **reset stored statistics** (although this is done with every push to the main):
         * Click the link to: [go to the **Generate Git Stats Images** GitHub Actions workflow](../../actions/workflows/non_auto_generate_stat_images.yml)
         > *This is required if the `actions_branch` branch is not created, as it is created when run*
      2. Otherwise, for **updating** generated statistics visualizations (although this is automatically done ):
         * Click the link to: [go to the **Auto Update Stats Images** GitHub Actions workflow](../../actions/workflows/auto_update_stat_images.yml)
         > *This requires the `actions_branch` branch to first be created with generated statistics visualizations*
   2. With the GitHub Actions page open, click the '***Run workflow***' dropdown menu button
   3. Select `Branch: main` from the '***Use workflow from***' dropdown list
   4. Click the '***Run workflow***' button
       * _Note: this could take some time_

### View Generated Statistics

5. Following the successful completion of a workflow, generated statistics visualizations can be viewed:
   1. In the `generated_images` directory in the `actions_branch` branch with the following image links:
      1. [Language statistics](../../blob/actions_branch/generated_images/languages.svg)
      2. [Overview statistics](../../blob/actions_branch/generated_images/overview.svg)

### Display Generated Statistics

6. To display the generated statistics, static URLs can be used for images that are updated weekly:
   1. For generated language statistics visualizations (replacing `<username>` with your GitHub username):
   ```md
   ![](https://raw.githubusercontent.com/<username>/GitStats/actions_branch/generated_images/languages.svg)
   ```
   2. For generated overview statistic visualizations (replacing `<username>` with your GitHub username):
   ```md
   ![](https://raw.githubusercontent.com/<username>/GitStats/actions_branch/generated_images/overview.svg)
   ```
   
</details>

# :closed_lock_with_key: Options

<details>
<summary>Click drop-down to view optional repository Secrets for customizing GitHub statistic visualizations
</summary>

* ### Optional Secret *Name*: `EXCLUDED`
  For excluding repositories from being included entirely in the generated statistic visualizations.
  
  **Instructions**:
  * enter *Value* in the following format (separated by commas):
    * `[owner/repo],[owner/repo],...,[owner/repo]`
  * example:
    * `jstrieb/github-stats,rahul-jha98/github-stats-transparent,idiotWu/stats`
* ### Optional Secret *Name*: `ONLY_INCLUDED`
  For **ONLY** including repositories in the generated statistic visualizations
    - such as when there are fewer repositories to include than to exclude
  
    **Instructions**:
    * enter *Value* in the following format (separated by commas):
      * `[owner/repo],[owner/repo],...,[owner/repo]`
    * example:
      * `R055A/GitStats,R055A/R055A`
* ### Optional Secret *Name*: `EXCLUDED_LANGS`
  For excluding undesired languages from being included in the generated statistic visualizations
  
  **Instructions**:
  * enter *Value* in the following format (separated by commas):
    * `[language],[language],...,[language]`
  * example:
    * `HTML,Jupyter Notebook,Makefile,Dockerfile`
* ### Optional Secret *Name*: `EXCLUDED_REPO_LANGS`
  For excluding any/all language statistics specific to a repository from being included in the generated visualizations
  
  **Instructions**:
  * enter *Value* in the following format (separated by commas):
    * `[owner/repo--language...--language],[owner/repo--language...--language],...,[owner/repo--language...--language]`
    * `--language` denotes a language in the repository to be excluded from stats or exclude this for all repo languages
  * example:
    * `jstrieb/github-stats--python,rahul-jha98/github-stats-transparent,idiotWu/stats--python--shell`
* ### Optional Secret *Name*: `IS_INCLUDE_FORKED_REPOS`
  Boolean option for including forked repositories in the generated statistic visualizations. These could repeat statistical calculations
    - `false` by default

  **Instructions**:
  * enter *Value* in the following format:
    * `<boolean>`
  * examples:
    * `true`
* ### Optional Secret *Name*: `IS_EXCLUDE_CONTRIB_REPOS`
  Boolean option for excluding non-owned repositories contributed to in the generated statistic visualizations
    - `false` by default

  **Instructions**:
  * enter *Value* in the following format:
    * `<boolean>`
  * examples:
    * `true`
* ### Optional Secret *Name*: `IS_EXCLUDE_ARCHIVE_REPOS`
  Boolean option for excluding archived repositories in the generated statistic visualizations
    - `false` by default
    
  **Instructions**:
  * enter *Value* in the following format:
    * `<boolean>`
  * examples:
    * `true`
* ### Optional Secret *Name*: `IS_EXCLUDE_PRIVATE_REPOS`
  Boolean option for excluding private repositories in the generated statistic visualizations
    - for when you want to keep those secrets locked away from prying eyes
    - `false` by default
    
  **Instructions**:
  * enter *Value* in the following format:
    * `<boolean>`
  * examples:
    * `true`
* ### Optional Secret *Name*: `IS_EXCLUDE_PUBLIC_REPOS`
  Boolean option for excluding public repositories in the generated statistic visualizations
    - `false` by default
    
  **Instructions**:
  * enter *Value* in the following format:
    * `<boolean>`
  * examples:
    * `true`
* ### Optional Secret *Name*: `MORE_REPOS`
  For including repositories that are otherwise not included in generated statistic visualizations when scraping by username
    - such as repositories imported from, say, GitLab - hint: add emails used in imported repo commits to profile settings
    
  **Instructions**:
  * enter *Value* in the following format (separated by commas):
    * `[owner/repo],[owner/repo],...,[owner/repo]`
  * example:
    * `R055A/GitStats,R055A/R055A`
* ### Optional Secret *Name*: `MORE_COLLABS`
  For adding a constant value to the generated repository collaborators statistic
    - such as for collaborators that are otherwise not represented
    
  **Instructions**:
  * enter *Value* in the following format:
    * `<int>`
  * example:
    * `4`
* ### Optional Secret *Name*: `ONLY_INCLUDED_COLLAB_REPOS`
  For **ONLY** including collaborative repositories in the generated average contribution statistics calculations
    - such as when there are fewer collaborative repositories to include than to exclude
  
    **Instructions**:
    * enter *Value* in the following format (separated by commas):
      * `[owner/repo],[owner/repo],...,[owner/repo]`
    * example:
      * `R055A/UniversityProject-A,R055A/UniversityProject-B`
* ### Optional Secret *Name*: `EXCLUDED_COLLAB_REPOS`
  For excluding collaborative repositories from being included in the average contribution statistics calculations
    - for example, such as for when 
      - contributions are made to a collaborative repo, but it is not one of your projects (open-source typo fix, etc)
      - someone deletes and re-adds the entire codebase a few times too many
      - your or someone else's performance is not fairly represented - missing data bias 
      - pirates, ninjas, etc.

  **Instructions**:
  * enter *Value* in the following format (separated by commas):
    * `[owner/repo],[owner/repo],...,[owner/repo]`
  * example:
    * `tera_open_source/bit_typo_fix,peer_repo/missing_or_no_git_co_author_credit,dude_collab/email_not_reg_on_github,dog_ate/my_repo,mars/attacks`
* ### Optional Secret *Name*: `MORE_COLLAB_REPOS`
    For including collaborative repositories that are otherwise not included in the average contribution statistics calculations
    - for example, such as when
      - nobody even bothered to join the repository as a collaborator let alone contribute anything
      - the repository is imported and because it is ghosted there are no other contributions and, thus, none of the other collaborators are represented in the scraping

  **Instructions**:
  * enter *Value* in the following format (separated by commas):
    * `[owner/repo],[owner/repo],...,[owner/repo]`
  * example:
    * `imported_ghosted/large_A+_collab_project,slave_trade/larger_A++_project`
* ### Optional Secret *Name*: `IS_STORE_REPO_VIEWS`
  Boolean for storing generated repository view statistic visualization data beyond the 14 day-limit GitHub API allows 
    - `true` by default

  **Instructions**:
  * enter *Value* in the following format:
    * `<boolean>`
  * examples:
    * `false`
* ### Optional Secret *Name*: `REPO_VIEWS`
  For adding a constant value to the generated repository view statistics
    - such as for when the stored data is reset or when importing stat data from elsewhere
    - requires being removed within 14 days after the first workflow is run (with `LAST_VIEWED`)
    - requires corresponding `LAST_VIEWED` and `FIRST_VIEWED` Secrets
    
  **Instructions**:
  * enter *Value* in the following format:
    * `<int>`
  * example:
    * `5000`
* ### Optional Secret *Name*: `LAST_VIEWED`
  For updating the date the generated repository view statistics data is added to storage from
    - such as for when the stored data is reset or when importing stat data from elsewhere
    - requires being removed within 14 days after the first workflow is run (with `REPO_VIEWS`)
    - may require corresponding `REPO_VIEWS` and `FIRST_VIEWED` Secrets
    
  **Instructions**:
  * enter *Value* in the following format:
    * `YYYY-MM-DD`
  * example:
    * `2020-10-01`
* ### Optional Secret *Name*: `FIRST_VIEWED`
  For updating the '*as of*' date the generated repository view statistics data is stored from
    - such as for when the stored data is reset or when importing stat data from elsewhere
    - may require corresponding `REPO_VIEWS` and `LAST_VIEWED` Secrets
    
  **Instructions**:
  * enter *Value* in the following format:
    * `YYYY-MM-DD`
  * example:
    * `2021-03-31`
</details>

# 🤗 Support the Project :green_heart:

There are a few things you can do to support the project (and that it is extended from):

- ✨ Star this repository (and/or 🌠 star [`jstrieb/github-stats`](https://github.com/jstrieb/github-stats) and 🔭 follow [`jstrieb`](https://github.com/jstrieb) for more)
- :memo: Report any bugs :bug:, glitches, or errors that you find :monocle_face:
- :money_with_wings: Spare a donation to a worthy cause 🥹

# 🫠 Note

The project was initially deployed to visualize a statistical representation of my historic university (collaborative) contributions - in the sense of code lines - and subsequently removed following negative feedback and other undesired consequences. 

The deciding factor was my assigned task work for another project pushed first by a co-collaborator, which coincidentally was very much the same API-fetching as in this repo, but for the first instance of the Data Engineering II course not starting until after the initial deployment of what this repository succeeds. This was before any deadline, without prior notification, but not before as-usual bend-over-backwards ever-committed sound planning and documentation, project/task management, and consistent communication otherwise, etc. And not before I explained and demonstrated to them how I am already doing it, as planned.

It is not the first time I have coincidentally completed assessment requirements unwittingly before beginning a course, or just truly completed prerequisites with undesirable consequences regardless of distinction in honest performance (and later employment for, but almost at the cost of my life, although any true understanding is cause for that, it would seem; TLDR) 🤔. I had no time remaining to supplement considering I was single-handedly challenging/surviving years of ongoing extremely far worse (underlying to this and countless more) circumstances in parallel under remote pandemic LOCKdown conditions with already a typical 3x average workload and 24/7 global timetable while then suffering from - the start/initial-exacerbation (of what is likely starting early 2019 - and by early I mean I'm up early always regardless of consistent nocturnal and other elusive attacks causing this) of what would become years of multiple mystery device-damage correlating head-to-toe severe - infections following countless other corresponding 24/7 seriously harmful and damaging issues too extent, extreme, complex, outrageously unimaginable, unbelievable, uncompromising, unyielding, unrelenting, unempathetically... insane, never-ending and simply out of my hands to write - and I've never been much of a fan of the Never Ending Snory (but thats just my bias, not that I've probably seen it too busy 24/7 surviving life attempts and eradications none-the-less since and throughout my very early childhood, and now my later one too - don't know whats more insane, this crap randomly existing still or my university supporting it as they have (including sabotage of the formal international exchange programme) regardless of blatant repeat evidence, all fact and simple common - doesn't take a rocket scientist to figure out -sense and knowledge, and lifetimes wasted repetitively cyclically forced to deal with this, or existing at all even; like their type, without multiple life imprisonments and the likes of "DJ cynds" who even randomly dropped her mic :((( at the mere sight of me nicely walking from A to B where I should rightly - although unrightly with an unjust burnt coffee - as if she ever existed to more than the half-dozen supporters not me until swapped last moment before bumwater election).

Thus, I do not know if the push made before mine passed, but we can assume anything not pushed by me, including none is instant global success. Still, at least they pushed something instead of the likes of harassing me or have me repeat it all in attempts to help them defraud being involved in mine, or just blatantly waiting until the deadline had passed to claim against documented evidence falsely and all other logic that I completed their task instead, or any other years-long backward misappropriation whether in parallel to cause biased feedback and grading or continuing as far as thesis (including report, research, etc - imagine [this main branch](https://github.com/University-Project-Repos/UU-Game) being claimed as solo thesis work using [this branch](https://github.com/University-Project-Repos/UU-Game/tree/GustavPelle) but after forced to wait weeks, or sprints, as if not always, for only them to get real - and needless to say why I'm not doing everything - in the first week or even day - is ethical collaborative intent and others not making their minds up for countless repeat meetings - when not declaring intent to do nothing or holidaying - of utter time wasting exclusion of author help to never reveal their only task responsible/"future-thesis" plan until the last moments and if this is the trend across projects then I have little time to spare, especially when those "responsible" for the project/task board aren't doing anything for completed task work to not be recognized) and just about anything and everything as always and beyond 🧐 for eg. Now imagine they're all - except for those less fortunate to not be born so to intimidate as them to not be "actively involved" - unable to speak good or any england until their perfectly written thesis to need the likes of me completing everything else with them. etc. etc.

Nut at all much different than those otherwise (digitally) defrauding me as not instead. For example, 2x 15/0.30 ECTS/EFTS worth - and effectively over 300/6 and much more - extensively documented git and other contributions - under consistent epic self-contradictory normalised deranged psychotic hysterical harassment and other intense undermining and (cyber) sabotage - blatantly defrauded - although exisiting clearly in presentation by others and their socio-technical system followed by the book - as nonexistent (and including all relevant - advanced real university - prerequisites in degree-level exacerbation?!) in meticulous - in the sense of lying down as if sleeping/"flying-high" across multiple seats in formal meetings - backward illogical labelling self-pittying unstable (with exception to the incessant Milli-Vanilli-level posing and random voice change - when not mumbling incoherrently (officially on the job) - to sound like a distant uncle) erratic despotic eternal-gaslight cultish compulsive creep physically (passive-)aggressive half-baked extortion eternally utmost disregarding all health and safety but their own (which in some health cases is the same in the underlying sense of motive but not the same sense of unsafe harm) and everything they simply should be doing - greater than that extorted from me without barely a finger lifted when not gaming or (years-druagged-24/7-harassing - all history and fact-of-matter reality overriding - random unnatural hypothetical) pretense normalised victim/fault blaming; TLDR (this alone is a climax of ongoing climactic insanity from years of all-educational institution and accommodation power and very real far worse abuse, and with those new involved already having a history to match) 🤷‍♂️ - at the end of the day it's an eternal struggle to cause this, but this shouldn't be just cause for a struggle to fix it, not that IT can fix their problems obviously giving cause why, although maybe now AI can a bit, but not even that - or even "nup!" - can help them pay for the harm and damages still incurring, not that payment will go to anyone but this type always being me and especially on the notion of what they portray as a problem they truly are being made right - if I'm in control, they're in control, etc. - if I'm writing bad because of their eternal crap - they never take - they're writing bad because of mine, etc. not that I can w/o the sky falling on my head as the only wrongdoing in their perspective is ever speaking their wrongdoings. And then when I'm the one working, everyone is the victim instead for all they can dishonestly portray with consistent undeserving credit regardless beyond imaginable - one just now consistently insanely pathetically illogically pretending to not understand anything and everything I painstakingly do to help them, not understanding they're not understanding prerequisite material for their degree entry let alone course, extremely rudely and aggressively holding up help for everyone else for hours at a time otherwise helped in minutes instead as if by caste, although I still somehow manage to help the same if not more than others somehow, or at least until they're working there instead of me in their perspectives, which they likely will be considering many I'm working with and sometimes under understand less.

Can't imagine how affected I am, but can imagine I've spent more than half my life 100% UNSUPPORTED INDEPENDENTLY recovering from injury alone (including throughout uni w/o recognition/representation of any  let alone any cause or other harm and damages - or at least until it was all over with one of the most outright backward of attacks in attempt to officialy rearrange defraud me of every exam I naturally honestly sat in representation as if it was never all under the un/misrepresented effects of consistent unforseeable attacks and other wrongdoings beyond my control, but rather some form of unknown special treatment truly received by many autistic psycho sadistic creep attacking me and countless others, and if not all credit altogether by trying my legal right - which, jokes on them, I never had not utterly violated along with all rules at all levels in every which way imaginable by them - to an education on for size - while randomly raving about more and more random citizenships and rights of plebs like me falling on their laps - they're probably kneck deep in stock rises, and better be with all owing if not mine outright since too, but how else can you ever make this up to them?!) and I'm not one to lose easy or mess up whatever way anyone wants to look at it. Writing this alone is testament to that considering the circumstances. I've recovered entirely from scratch many times in more ways imaginable to even myself today, whether from significant physical movement impairment, all motor skill loss, eye sight, hand-eye coordination, all memory, skill, understanding, etc. I guess it's a good thing I did good or more than beforehand and in-between to somewhat repeat recover back to, although the first is probably 12/13, and its more surgery than recovery, although with permanent significant technical damage but I'm already playing physical sport in international tournaments in my first season and parading for royalty then during (or after the removal) of it, etc. Not to mention the years of sleep deprivation - many can afford to cause this without day jobs to not quit somehow?! - and non-physical harm, etc - I am being globally (cyber) stalked and digitally attacked (including at least attempted manslaughter) consistently throughout (or at least since they stopped attempting full-frontal such attacks, theft and other criminality, which I can't imagine why this would transition online as I transition in recovery), for eg. - and certain my bag is an online target now by angry loser bums of the century when (I wish could say only budget) flying too (enough to write a book about alone, which ironically could just be why it's targetted by such type in the first place) and on the bus from uni with consistent door close/open attacks - or I'm just a night owl nocturnally terrorising and torturing myself (just when not home - no, they attack that now too, and everywhere else I go when digital), etc.

Basically, for all I do good (and real or just remotely rationale) - which is all I seem to do - especially for others, all I can do is bad in these environments. Many do nothing ever, as the statistics suggest. Many proclaim this as their intent (keep in mind some can afford to neglect their obligations when involved in certain societies, or think so, or outright purchase my life by purchasing education before they can legally work (which I was technically doing back when parading for royalty)?! or not spending farm land inheritance in life obsession etc), even going as far as stating they neither can nor care to understand the material - whether taught or prerequisite - and then randomly claim interferance (unprofessionalism, etc) after project completion somehow regardless of countless opportunity tirelessly ignored with exception to (anything and everything but collaboration) interferrence only by them. Can you believe such \*overdramatic reactions before anything ever\* delusions can become my (elusive, warping the Agile methodlogies I taught years prior maliciously controlling against me and the projects chance of success, and reverting back to why I used those methods in the first place - not that any method can prevent the most crucial of critical pushes faster than the speed of light not reviewed (and thus not PR-merge committed - although anyone can just click the PR link to see the true push commit datetime stamps) until the final moments if even the same sprint if you can call thoroughly repetitively teaching the reviewer the material in-person all-day as they tirelessly (as always fruitlessly; just like one of my many life obsessors always challenging and then being me somehow also still not leaving uni alone, of which they remind me too much of) aggressively persist to test in pretense for their presentation as you until you're naturally forced to correct or finish it) project supervisor? - as if this isn't the only viable pathway for their type only ever working on those working on the work. Not hard to imagine when all lectures are not being given until last moment late in course - by those with histories travelling to true crime hotspots - to immediately "catch out" on camera those with timetable change clashes as "freeriding" instead?! Or just blatantly claiming those only doing the only evident work to be only not the moment they're unwell with the likes of covid just on the outbreak of the global pendemic. They call it (Eastern ponzi?!) business, but only after the business, and only for themselves - as if any business they touch can ever be for anything else not ruined (at least with me existing in it somewhere somehow) - and if not "engineer" (always; like my test results, although I also get ESTJ so who knows, or my degree and corresponding studies) while others engineering (always) in "study". It could be worse, it could be my home university. Everything for nothing, nothing for everything. FTR, my group project contributions are always naturally gradual in utmost collaborative intent with others, and never all pushed at the beginning as some others do to just ghost without understanding of the material. If ever most or all contributions are by me it is only by necessity in the final moments of a deadline when no other option is available, and always at zero expense to others (with no true task of others interferred with) and ultimate expense otherwise.

Ironically, I deployed this for a finally once fair understanding of my general position under such biased dishonest (and unimaginably far worse if not the worst ever in at least local history if not all) circumstances spanning back as far as 2014 (although it is obvious the conspiracy has roots far beyond this, and in cases, if not all, since I was a toddler, if not since ever). The Data Engineering II course was also the first case of individual project contributions having any significance in grading at that university. I left my old university because of such organised behaviour, although now all one needs is LLM (such as cheat-GPT), which is also used as a weapon with the historic transition instantly noticeable in behaviour as experienced (with a sudden overnight influx of real noob competition not needing me or mine to not be needed ever by anyone, for eg). At least now I can spot any kind of cheat. Much motive in wrongdoing against me in education is connected to the dishonest practices of others, whether individual or group conspiracy, much undeniably evident whether then or now although always to me. This is just happening today at my recent uni in eternal repetition of history there too with blatant random irregular manipulating dishonesty ringing eternally ignored alarm bells, which is also evident in employment with consistent fruitless passive-aggressive invalid (voluntary disclosure pretext) "invalid" desperate schizo stitch-up gaslighting obstructive and obfuscating noob attacks - disgruntled before any work (which is eternal in some cases) let alone grading - staring me in the face - but 1 in 1000 aren't such bad odds, or should I say 1 in 3 when it's those I'm replacing, if you can ever call it that judging from what I'm seeing contributed from them, or not ever, or am I looking at it back-to-front?! I can coincidentaly also spot true crime and bs from a mile away since very young too.

GitStats is nothing personal, but only for reflective natural understanding in any circumstance, and is neither (the likes of) a planned jihad nor represents the statistics of any other collaborator. This can be seen for oneself by deploying individual GitStats repositories using this as a template (instructions are in this README.md). The statistics do not, however, represent correctness or underlying dynamics, etc., although I can confirm all my university contributions pass with distinction on average and only include code of significance (that is, exclude redundant configuration files, unchanged rewritting of the code base pushes & other git-misuse, etc.). On the note of distinction, I should mention though that just because I may not have such a grade in a project/course does not mean my performance is not equal to this. For example, one advanced project course I have 21/22 or 22/23 etc points and scored over 90% in the exam, but because of one error (which is all by me in the perspectives of those hating) in instruction have the same grade somehow as anyone not required to do anyting but score at least 20% in the exam regardless of multiple significant practical project components of the course, and although my contributions are probably also over 90% they are not included in the statistical averaging anyway with the project extending on an already extensive open-source legacy codebase, and not that documentation, such as PR reviews etc will also be included.

# ae-interview

I'll use this repository as a way to keep track of my process and thinking for
the Jukebox exercise.

My goal is to show you my process through the git history.

Since I'm doing this on a weekend, I'm going to answer my own questions.
Normally, I'd ask the team or go through a brainstorming session for ideas.


## Notes
Initial read through

- 1 Jukebox - N Albums
- 1 Album - N Songs
- Users should be able to select songs with a five-character identifier
  - two-digit ID for the album, a hyphen, and two-digit ID for the song.
  - Ex. "01-04"
- As users select songs, the songs should be added to a play queue. Songs should be played in the order they are selected.

- Adding 1 song to the queue costs one credit.
- Credits are purchased by the user in whole-number dollar amounts
  - $1 dollar = 3 credits
  - $2 dollars = 7 credits
  - $5 dollars = 18 credits
- Any positive whole number should be accepted

Jukebox should be able to:
- List available albums and songs with their appropriate(<- this word is spelled incorrectly in the PDF) ID's
- Accept dollar amounts and credit the user appropriately
- Add new songs to the queue
- Report the song currently playing
- Report the next song to play

While not part of current requirements, think of HTTP API design.


------------------------
Okay, some interesting parts to this exercise!

? - Questions up front - Parenthesis are my assumptions:
- What happens if we add more than 99 albums to the jukebox? (No)
- What happens if an album has more than 99 songs on their one album? (Won't happen)
- Where is this jukebox going to be installed? Restaurant, bar, website, etc.? (It's going to be installed at a Chili's)
- How many users do we expect to use the jukebox concurrently (if software only)? (1 user per session, need to keep track of users and their credits)


Order of how I usually think of problems
1. What tools are available to solve this? (Don't reinvent the wheel)
2. What does the data look like? (SQL/NoSQL options)
3. What does the logic look like? (Software Design/Architecture)
4. What does the UI/UX look like? (Is it easy to use?)
5. Are we using CI/CD? (Ansible, Jenkins, GitHub Actions, etc.)
6. Prototyping

### 1
Since I'm going to build this, I'll just assume that number 1 doesn't apply.

### 2
Typically, I like to work with the data next before I even start coding.
I need to see the representation of it. Usually in some sort of SQL table format.
Initially, the implementation will all be in memory using python 

- User
id | Name | Credits
- Album
id | title | artist
- Song
id | album_id | title | duration

For now, this will be the database. Playlist will be a python queue in memory.
It would need to know the following
- Five-Character song identifier
- (Added after) User that selected the song

? - Question
- Would we want to keep track of Playlist history? If so, how long should the
history be? (For now, no. In the HTTP API version yes.)
- Should the playlist alse keep track of the User that selected the song? (Yes)
- What does the User authentication look like? (Simple version, User select 
    their name from a list or adds new entry. HTTP API - Username/Password needed)

### 3
Now that I have a general idea of the way the data looks like, I typically go to
design. The essential question I'm asking is "How can I logically chunk this?"
As part of this, I also like to think of whether we need parallelism and
concurrency but in this case, I'll save the that for the HTTP API

- User creation flow
- User payment/credit flow
- User song selection flow
- Playlist queue flow
- Music Player flow (Songs get "played" here)
- Admin/Secret album/song management flow. We want to be able to update the
    catalog, not the users.


### 4
UI/UX I usually draw using this program called "Concepts" on my iPad that has
an infinite sketching area. But since we're going full text based today, I'm
going to do something REALLY simple. I may try to use `rich` or `Textual` to 
build the UI in the terminal but it's a stretch.

Currently Playing
-------------------
<Time:Left> - ~* <Song Title> *~
Up Next: <Next Song Title>

-------------------
Logged In: <User>
-------------------
Options:
1. Select User
2. Pay for Credits
3. Select next song


### 5
For this example, I'm going to leave CI/CD for later. This is usually very
company driven and everyone has their own way of doing it. The simplest
CI/CD is git push locally, SSH into a machine, git pull, restart services.
If I have time, my initial intuition is to use a docker container and a
kubernetes cluster.


### 6
I like to use TDD, especially in the prototyping phase because adding tests
after a lot of code has been written is a pain. For this example, I'll also
start with `poetry` for the packaging.
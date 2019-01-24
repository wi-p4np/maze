
## General description
Project implemented as part of an internal programming course - Python for non-programmers at WebInterpret.
The goal of the project is to create a maze game.


## F.A.Q.
### How can I download this repository?
1. Make sure you have git installed on your computer, use following link to download it: https://git-scm.com/downloads
2. Make sure you have created a github account
3. Generate ssh key and add it to github, see following link: https://help.github.com/articles/adding-a-new-ssh-key-to-your-github-account/
4. Open terminal and go to directory where you want to store the repository.
5. Use following command to clone the repo: `git clone git@github.com:wi-p4np/maze.git`


### How do I update my repository?
You should always update your repository before you start working!
1. Open terminal and go to this repository
2. Type `git pull`
3. If there was other changes git will try to automatically merge them with your current project.
4. If you have modified the same files as someone else, there can be a conflict in the merge

### How to solve a conflict?
1. Start with running `git status` and find files that were marked as `both modified`
2. Now you will need to fix each file, one by one.
3. Open file with your favourite editor.
4. In a file you will see something like this:
 ```
 <<<<<<< HEAD
 Their changes
=======
Your changes
>>>>>>> branch-a`
 ```
5.  Delete the conflict markers `<<<<<<<`, `=======`, `>>>>>>>` and make the changes you want in the final merge.
For example: leave only `Your changes` and delete other text and all `>`, `=` and `<`.
6. You need to add those modified files using `git add <file_name`.
7. Then you can commit the merge typing `git commit` it will automatically create a commit message.

### How can I start working on new task (creating a branch)
1. Start with creating a new branch for your task
2. Make sure you are on master branch: `git checkout master`
3. Pull current changes with `git pull` (if there are conflict, try solving them using a description above)
4. Create your branch typing: `git checkout -b <name_of_your_branch>`,
For example: `git checkout -b adding_new_magic_spells`
5. Now you are on your new branch. You can start creating your commits here.
6. You can check between existing branches using: `git checkout <name_of_branch>`
7. Now, if commit any changes there will be send to your branch.
8. To push your branches to remote: `git push origin <name_of_your_branch>`

### How can I commit my changes?
1. Open terminal and go to this repository
2. Check you current changes in repository. Type: `git status`
3. Check if all modified files are listed, if not, make sure you saved all your files.
4. Add files to commit.
- If you want to add all files to commit, use `git add .`
- If you want to add just selected files, use `git add <file_path>` for each file
5. Create a commit. Type `git commit`
6. Type commit message explaining your changes and save.
7. Push your commit to your branch. Type: `git push origin <name_of_your_branch>`.


### How can I merge my changes with master?
1. Commit all your changes and push your branch to remote. 
2. Go to github page of our project.
3. Find button `New pull request` and click it
4. Select your branch from the list and click `Create pull request`

## Authors
- @heolin123
- @dennise909
- @myriam-lp
- @elena-gre
- @ilaria-neg

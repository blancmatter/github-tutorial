# Rewinding to a previous state

This is used if we have broken our code or want to get hold of some data that we previously deleted / overwrote.

**This is complicated**, so the below is details of how to do this easily without getting confused. Once you have this operation understood, and you want to confuse youself, see;
https://opensource.com/article/18/6/git-reset-revert-rebase-commands


## Our basic reverting method

We are going to use a 'bodge' to go back to a previous state, or partially to a previus state. The steps are;

* Checkout an old commit were we have data we want to return to
* Copy the files out to another location
* Go back to the `HEAD` of the `main branch` (the default branch)
* Overwrite the files with the ones we copied away
* Recommit to make the changes


### Checkout a previous commit

* First make sure we are in a clean situation with no uncommited changes
    ```shell
    $> git add -A
    $> git commit -m "This is a commit, all up to date"
    ```

* Check the commits using `git log`;
    ```shell
    $> git log --oneline
    4bbf5b5 (HEAD -> main, origin/main, origin/HEAD) Merge branch 'test' into main
    2abb7be (test) Checking rewind
    e51d923 Added image
    89bba62 Changed image format
    4734d07 Fixing image
    ```

* Checkout the commit that has the state we want to get back to
    ```shell
    $> git checkout 89bba62
    ```

* Then we need to copy away the files we want to revert to. This can be done on the command line or using the file browser
    ```shell
    $> cp <files I want> /tmp
    ```

* Next we will go back to the most current commit. As we are on the `main` branch (or might be called `master` if created in git) we do;
    ```shell
    $> git checkout main
    ```

* So we have copied away the files we want to revert to, and are at the main branch head. We copy back the files and then commit the changes. Do this is a file browser if this seems easier
    ```shell
    $> cp /tmp<files I want> ./
    $> git add -A
    $> git commit -m "Reverted files back to working state"
    ```


## Next Page
Pushing and pulling to/from github - [pushpull-github.md](pushpull-github.md)

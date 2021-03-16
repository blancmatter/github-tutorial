# Pushing and Pulling to/from github

This is useful for knowing that your code is backed up. It will also allow you
to run and develop code on your Laptop/Desktop and transfer updates to
computing clusters if you are using them.


## Pushing and pulling to github
As we cloned from github the `local` repository knows where the `remote`
repository is. This is called `origin`

* To push our latest updates on the `main branch`, we do;
    ```shell
    $> git push origin main
    ```

* If we then change our code from another machine, or on github itself, we need
to make sure the `local` and `remote` stay in sync. **Do not change any
files locally and remotely at the same time!**
    ```shell
    $> git pull origin
    ```

## What if we get in a mess???
If the local and remote get out of sync it can be a right faff! in this
situation our 'bodge' is to;
* Copy any files we have changed locally to a temporary location
* Delete the repsotistory locally **MAKE SURE THERE ARE NO UNTRACKED FILES YOU NEED**
* Re `clone` the repository from github
* Add any changes back in
* Commit
* Push back to github any changes

This may look something like;
    ```shell
    $> cp <files I need> /tmp
    $> cd ../
    $> rm -rf <mygitrepository>
    $> git clone https://github/com/<username>/<mygitrpository>
    $> cd <mygitrepository>
    $> cp tmp/<files I need> ./
    $> git add -A
    $> git commit -m "This is my synchronised git commit"
    $> git push origin main
    ```


## Next Page
**BONUS** - branches and why you don't want to use them - [branching-workflow.md](branching-workflow.md)

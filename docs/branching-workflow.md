# Branching and why you don't want to use it!

Branches are super helpful and a core concept of git and github. They are
mentioned here for the keen.

See these resources for more info and exercises.
https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow
https://learngitbranching.js.org/

## Development Workflow
The workflow is as follows;

* Create and checkoput a new branch
```shell
git checkout -b <branch-name>
```

* Develop and commit and push branches to the `remote` as we develop

    ```shell
    $> git add -A
    $> git commit -m "Commit message"
    $> git push origin <branch-name>
    ```

* When ready we can merge back to main branch first we need to make sure there
are no uncommited chnages on our branch, checkout the main branch, then merge
    ```shell
    $> git add -A
    $> git commit -m "Ready to merge"
    $> git checkout main
    $> git merge <branch-name>
    ```

* The `main` branch now has all the changes of the branch

## Next Page
Exercises in github - [exercises.md](exercises.md)

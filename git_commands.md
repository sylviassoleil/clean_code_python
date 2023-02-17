#todo  Figure out how to split the merge request... 

reset soft ~ HEAD 

### to split the git commits 
- main branch: main
- dev branch: dev_0
- dev branch 1: dev_1\

scenario: move some of a bunch of commits originally on dev_0 to another branch dev_1\
dev_0 commits: A-B-C-D-E-origin master\
Target:\
dev_0: C-D-E-origin master\
dev_1: A-B-origin master\



currently on dev_0\
``` git checkout -b dev_1 ```

commits: A-B-C-D-E\
``` git rebase -i <SHA of the last commit origin master>```

in the cherry-pick doc, `Vd` the lines to ignore 
``` 
pick A
pick B
pick C #to delete
pick D #to delete
pick E #to delete
```

then save the file with `:wq`

```git push -f origin dev_1```

get back dev_0 

```
git checkout dev_0 
git reset --hard <reset commit C>
```




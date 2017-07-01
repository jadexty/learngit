Gpush

To push the current branch and set the remote as upstream, use

git push --set-upstream origin master

此时如果origin的master分支上有一些本地没有的提交,push会失败.

所以解决的办法是, 首先设定本地master的上游分支:

Git branch --set-upstream-to=origin/master

　　然后pull:
!git pull --rebase

　　最后再push:
Git push

Git push origin study_git
Git 等于!git


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
就ok了

Git 等于!git

git log --graph --pretty=oneline --abbrev-commit

#git branch -d study_git 出现错误:
C:\windows\system32\cmd.exe /c (git branch -d study_git)
warning: not deleting branch 'study_git' that is not yet merged to
         'refs/remotes/origin/master', even though it is merged to HEAD.
error: The branch 'study_git' is not fully merged.
If you are sure you want to delete it, run 'git branch -D study_git'.
shell returned 1
Hit any key to close this window...
#用git status 检查了两个branch, 都没有modified的文件, 所以就强制删除吧

git branch -D study_git

最后就留有master这个分支.

#------------------------------------------------------------
1.建立一个byl的branch, 修改test文件,增加一行内容"捕鱼来了", 保存退出. 用add和commit命令,提交到库.

checkout 到master分支, 直接用merge合并byl这个分支, 会提示forward, 表示前进, 因为master这个分支在时间线上落后了. 

操作要在test这个窗口
Git branch byl
Git branch 
Git add %
Git commit -m "create byl branch and add 捕鱼来了 in test file"
Git status --untracked-files=no
Git log
Git checkout master 
Git branch
*master表示当前分支是master
Git merge byl
Git branch
在输出窗口,可以用q,退出窗口.
Git branch -d byl 删除byl分支.

2. 建立一个分支byl,修改test文件,增加一行内容"捕鱼来了,小心啊",保存退出. 用add和commit, 提交到库,用status查看库状态,log会有记录.

checkout到master分支,如果test文件正在被打开,会提示文件被修改, 选择ok.  修改test文件, 增加一行内容"master 捕鱼来了", add和commit提交到库.

merge byl分支, 会提示有conflict , 打开test文件,会有<<<<<表示冲突的地方, 修改为"捕鱼来了". 再次add 和commit,然后merge, 就不会有冲突提示了. 

Git branch -d byl 删除byl分支,也不会有错误提示, 除非你没有修改冲突,并且提交到库.

Git checkout -b byl

Git push

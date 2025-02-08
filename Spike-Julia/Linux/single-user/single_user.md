# CentOS 7进入单用户模式(single user mode)

**忘记root密码时，进入单用户模式，通过重新设定密码的方式，来重新登入**

1. 开机，`Ctrl+G`进入虚拟机

![](https://github.com/Spike-Julia/markdown-photos/blob/main/Spike-Julia/Linux/single-user/Snipaste_2023-12-02_10-22-55.png?raw=true)

2. 按下`e`键(edit)，进入编辑模式，初次进入界面如下

![](https://github.com/Spike-Julia/markdown-photos/blob/main/Spike-Julia/Linux/single-user/Snipaste_2023-12-02_10-24-10.png?raw=true)

3. 定位到`linux16`一行，将`ro`更改为`rw`，将`zh_CN`更改为`en_US`，删去`rhgb quiet`，并在`UTF-8`后输入`init=/bin/sh`

如下图所示![](https://github.com/Spike-Julia/markdown-photos/blob/main/Spike-Julia/Linux/single-user/Snipaste_2023-12-02_10-47-58.png?raw=true)

```shell
ro --> rw : 以"只读"模式挂载  --> "读写"模式挂载
zh_CN --> en_US : 中文 --> 英文 		ps:否则`提示信息不能正确显示`
rhgb quiet删去 : 不以图片格式加载,像命令行一样滚动
init=/bin/sh : 准备初始化
```

`Ctrl+x`进入执行

![](https://github.com/Spike-Julia/markdown-photos/blob/main/Spike-Julia/Linux/single-user/Snipaste_2023-12-02_10-48-49.png?raw=true)

等待一会后，会出现初始化完成的样子

![](https://github.com/Spike-Julia/markdown-photos/blob/main/Spike-Julia/Linux/single-user/Snipaste_2023-12-02_11-25-19.png?raw=true)

输入`passwd`来重置`root`用户的密码

![](https://github.com/Spike-Julia/markdown-photos/blob/main/Spike-Julia/Linux/single-user/Snipaste_2023-12-02_11-27-55.png?raw=true)

接下来输入新密码，比如`123456`

![](https://github.com/Spike-Julia/markdown-photos/blob/main/Spike-Julia/Linux/single-user/Snipaste_2023-12-02_11-30-13.png?raw=true)

如果输入不匹配

![](https://github.com/Spike-Julia/markdown-photos/blob/main/Spike-Julia/Linux/single-user/Snipaste_2023-12-02_11-31-54.png?raw=true)

重新执行一遍上述操作

![](https://github.com/Spike-Julia/markdown-photos/blob/main/Spike-Julia/Linux/single-user/Snipaste_2023-12-02_11-33-07.png?raw=true)

重置密码成功

![](https://github.com/Spike-Julia/markdown-photos/blob/main/Spike-Julia/Linux/single-user/Snipaste_2023-12-02_11-36-37.png?raw=true)

```shell
touch /.autorelabel     //使得 SELinux 生效，必须执行，否则无法重启
exec /sbin/init    //初始化和启动系统
```

接下来就是等待重启

这是删除`rhgb quiet`的界面，命令行滚动

![](https://github.com/Spike-Julia/markdown-photos/blob/main/Spike-Julia/Linux/single-user/Snipaste_2023-12-02_10-53-22.png?raw=true)

未删除`rhgb quiet`的界面，图形化，需要等待一会

![](https://github.com/Spike-Julia/markdown-photos/blob/main/Spike-Julia/Linux/single-user/Snipaste_2023-12-02_10-41-36.png?raw=true)



这是中文乱码，尽管两次均输入`123456`，仍不行

![](https://github.com/Spike-Julia/markdown-photos/blob/main/Spike-Julia/Linux/single-user/Snipaste_2023-12-02_10-32-22.png?raw=true)



[CentOS7 修改root密码,进入单用户模式(运行级别1)——实测有效！_centos7 rw rhgb-CSDN博客](https://blog.csdn.net/Yuanyi_1/article/details/104734011)

[系统运维|以单用户模式启动 CentOS/RHEL 7/8 的三种方法 (linux.cn)](https://linux.cn/article-12181-1.html)

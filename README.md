# srt-process
一个可以快速删除 srt 字幕文件中英文字幕的程序

## 使用方法：
 1. 将字幕文件和程序放在同一文件夹下
 2. 命令行下运行 `python process.py filename`
 3. filename 是待处理的字幕文件名，带不带扩展名都可以，因为如果没有扩展名的话，程序会自动在文件名后面加上 “.srt"
 4. 当前目录下生成 new_filename 文件，检查无误后，删除前缀 ”new_"后移动到`zh-cn`文件夹
 
## 图片示例：
 
 1. 处理前<br>
 <img src="https://raw.githubusercontent.com/slimwang/srt-process/master/img/before.png" width="480">
 2. 处理中<br>
 <img src="https://raw.githubusercontent.com/slimwang/srt-process/master/img/shell.png" width="480">
 3. 处理后<br>
 <img src="https://raw.githubusercontent.com/slimwang/srt-process/master/img/after.png" width="480">

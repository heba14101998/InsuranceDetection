# **Linux cheat sheet**

### **Directory Operations**
| Command | Description |
|---------|-------------|
| `pwd` | Print current working directory |
| `mkdir dir_name` | Create a new directory |
| `mkdir -p dir1/dir2/dir3` | Create nested directories |
| `cd dir_name` | Change directory |
| `cd ..` | Move up one directory |
| `cd ~` or `cd` | Go to home directory |
| `cd -` | Switch to previous directory |
| `ls` | List files and directories |
| `ls -l` | Detailed list (permissions, size, etc.) |
| `ls -a` | Show hidden files (starting with `.`) |
| `ls -lh` | Human-readable file sizes |
| `tree` | Display directory structure (install with `sudo apt install tree`) |
| `rmdir dir_name` | Remove an **empty** directory |
| `rm -r dir_name` | Delete directory **and contents** (⚠️ **Dangerous!**) |
### **File Operations**
| Command | Description |
|---------|-------------|
| `touch file.txt` | Create an empty file |
| `cat file.txt` | Display file content |
| `less file.txt` | View file page by page (`q` to quit) |
| `head -n 5 file.txt` | Show first 5 lines |
| `tail -n 5 file.txt` | Show last 5 lines |
| `tail -f file.log` | Follow log file updates in real-time |
| `cp file.txt newfile.txt` | Copy a file |
| `cp -r dir1 dir2` | Copy a directory recursively |
| `mv file.txt new_name.txt` | Rename or move a file |
| `mv file.txt ~/Documents/` | Move file to another directory |
| `rm file.txt` | Delete a file |
| `rm -i file.txt` | Delete with confirmation |
| `rm -f file.txt` | Force delete (no warning) |
| `rm -rf dir_name` | ⚠️ **Force delete directory & contents!** |
### **File Permissions & Ownership**
| Command | Description |
|---------|-------------|
| `chmod 755 file.sh` | Change permissions (read/write/execute) |
| `chmod +x script.sh` | Make file executable |
| `chown user:group file.txt` | Change owner & group |
| `chown -R user:group dir/` | Recursively change ownership |
### **Search & Find Files**
| Command | Description |
|---------|-------------|
| `find /path -name "*.txt"` | Find files by name |
| `find / -type f -size +10M` | Find files >10MB |
| `grep "text" file.txt` | Search for text in a file |
| `grep -r "text" /path/` | Recursively search in directories |
### **Compression & Archiving**
| Command | Description |
|---------|-------------|
| `tar -cvf archive.tar dir/` | Create a tar archive |
| `tar -xvf archive.tar` | Extract tar archive |
| `gzip file.txt` | Compress file (creates `file.txt.gz`) |
| `gunzip file.txt.gz` | Decompress `.gz` file |
| `zip archive.zip file.txt` | Create a ZIP file |
| `unzip archive.zip` | Extract ZIP file |
### **⚠️ Dangerous Commands (Use with Caution!)**
- `rm -rf /` → **Deletes everything!** (Never run as root!)
- `chmod -R 777 /` → Makes all files executable (security risk!)
- `:(){ :|:& };:` → Fork bomb (crashes system!)
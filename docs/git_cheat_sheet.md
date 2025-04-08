# Basic Git Cheatsheet 🌿

## 🏁 Getting Started
```bash
# Set your info (do this once)
git config --global user.name "Your Name"
git config --global user.email "your@email.com"

# Start a new repo
git init

# Download a project
git clone <project-url>
```

## 🔄 Daily Workflow
```bash
# Check what changed
git status

# Stage changes
git add <file>       # Single file
git add .            # All files

# Save changes
git commit -m "Describe your changes"

# Send to GitHub/GitLab
git push origin <branch-name>

# Get updates
git pull origin <branch-name>
```

## 🌱 Branch Basics
```bash
# Make new branch
git branch <branch-name>

# Switch branch
git checkout <branch-name>

# Make AND switch (shortcut)
git checkout -b <branch-name>

# List branches
git branch
```

## 🔀 Merging (New!)
```bash
# Merge a branch into your current branch
git merge <branch-to-merge-in>

# Example workflow:
git checkout main          # Switch to main branch
git merge feature-branch   # Bring in the changes
git push origin main       # Update remote
```

## ⏪ Fixing Mistakes
```bash
# Undo unstaged changes
git checkout -- <file>

# Unstage a file
git reset <file>

# Change last commit
git commit --amend -m "New message"
```

## 📜 View History
```bash
# Show commits
git log

# Compact view
git log --oneline

# See changes
git diff
```
> Replace `<...>` with your actual values



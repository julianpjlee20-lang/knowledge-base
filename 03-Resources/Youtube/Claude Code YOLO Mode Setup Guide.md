# Claude Code YOLO Mode Setup Guide

**Source:** [Use Claude Code in auto-pilot (SAFELY!)](https://www.youtube.com/watch?v=8dqqa0dLpGU)
**Author:** Ian Nuttall
**Date Created:** 2025-07-01

## Overview

This guide explains how to run Claude Code in "YOLO mode" (dangerously-skip-permissions) safely using Docker Dev Containers. This allows Claude to work autonomously without asking for permission for every action.

### What is YOLO Mode?

YOLO mode uses the `--dangerously-skip-permissions` flag that bypasses all permission checks, letting Claude work uninterrupted until it completes tasks. Anthropic engineers use this method themselves, often letting Claude work autonomously for 30 minutes.

### Use Cases

- Fixing lint errors
- Generating boilerplate code
- Installing new projects
- Debugging applications in readonly mode
- Spinning up brand new sites

### Security Risks

Without protection, Claude could potentially:
- Delete files or entire hard drives
- Visit websites with prompt injection
- Execute harmful commands unintentionally

**Solution:** Use Docker Dev Containers to isolate Claude's operations

---

## Prerequisites

### Required Software

1. **Docker Desktop**
   - Download from: https://docker.com
   - Install for your operating system (Mac/Windows/Linux)

2. **VS Code or Cursor IDE**
   - Dev Containers extension by Microsoft

3. **Claude Code**
   - Must have Claude subscription (Claude Max recommended)

### Required Extensions

- **Dev Containers** extension (by Microsoft/Anthropic)

---

## Step-by-Step Setup

### Step 1: Clone the Claude Code Repository

1. Go to the Claude Code repository
2. Click the "Code" button on the right side
3. Copy the repository URL

4. Open your terminal (Warp, iTerm2, or any terminal)

5. Clone the repository:
```bash
git clone [paste-repository-url]
```

6. Navigate into the cloned folder:
```bash
cd claude-code
```

### Step 2: Clean Up Unnecessary Files

1. View all files including hidden ones:
```bash
ls -la
```

2. Keep only the `.devcontainer` folder (everything else can be deleted)

3. Delete unnecessary files:
```bash
# You can do this manually or use your terminal in agent mode
# Keep only: .devcontainer folder
```

### Step 3: Open in Your IDE

1. Open the folder in Cursor or VS Code:
```bash
code .
# or if using Cursor with custom alias:
vs .
```

### Step 4: Modify the Dev Container Configuration

**Important modifications to `.devcontainer` files:**

#### Modification 1: Persistent Authentication

**Purpose:** Avoid re-authenticating every time you open the container (especially important for Claude Max users)

**Location:** `.devcontainer/devcontainer.json`

**Change the mount method:** Update the mounts configuration to persist authentication tokens

#### Modification 2: Port Forwarding (for web apps)

**Purpose:** Access your app outside the container (e.g., Next.js apps)

**Add to configuration:**
```json
"forwardPorts": [3000],
"portsAttributes": {
  "3000": {
    "label": "Next.js App"
  }
}
```

**Note:** Adjust port number based on your framework (3000 for Next.js, 8000 for Django, etc.)

### Step 5: Initial Container Setup

1. Open Command Palette:
   - **Mac:** `Cmd + Shift + P`
   - **Windows/Linux:** `Ctrl + Shift + P`

2. Type: `Dev Containers`

3. Select: **"Open Folder in Container"**

4. Select the `claude-code` folder

5. Press **Enter** to name it (or keep default)

6. Wait for the container to build (first time takes a while)

### Step 6: First-Time Claude Code Setup

Once the container loads:

1. Type in terminal:
```bash
claude
```

2. Complete the first-time setup:
   - Log in with your Claude subscription
   - Use recommended settings
   - Trust the files in the folder
   - Allow Cursor extension installation

3. Exit after setup is complete

### Step 7: Reopen and Test

1. Close the container

2. Open Command Palette again (`Cmd/Ctrl + Shift + P`)

3. Type: `Dev Containers`

4. Select: **"Reopen in Container"**

5. Notice how much faster it opens the second time

6. Test authentication:
```bash
claude
```

You should log straight in without authentication prompts.

### Step 8: Enable YOLO Mode

1. Exit Claude if running

2. Start Claude with YOLO mode:
```bash
claude --dangerously-skip-permissions
```

3. Accept any initial prompts

4. Claude will now work autonomously without asking for permission

---

## Using YOLO Mode

### What Claude Does Automatically

- Runs bash commands without confirmation
- Makes file edits without asking
- Installs packages and dependencies
- Runs development servers
- Makes multiple changes in sequence

### Example Session

```bash
claude --dangerously-skip-permissions
```

**Prompt:** "Create a new Next.js app with TypeScript"

Claude will:
1. Run `npx create-next-app` with appropriate flags
2. Answer setup questions automatically
3. Make configuration changes
4. Start the development server
5. Report completion

### Accessing Your App

If running a web server (like Next.js on port 3000):

1. Look for the "Open in Browser" notification
2. Click to open your app
3. The forwarded port makes it accessible outside the container

---

## Troubleshooting

### Issue: Turbo Pack Compilation Error

**Problem:** Next.js site won't compile with Turbo Pack enabled

**Solution:** 
1. Open `package.json`
2. Remove the `--turbo` flag from the dev script
3. Restart the development server

### Issue: Port Not Accessible

**Problem:** Can't access the app in browser

**Solution:**
- Verify port forwarding is configured in `.devcontainer/devcontainer.json`
- Check the correct port number matches your app
- Restart the container

### Issue: Authentication Required Every Time

**Problem:** Claude asks for login on every container restart

**Solution:**
- Verify mount configuration changes were saved
- Rebuild the container completely
- Check file permissions on mounted volumes

---

## Best Practices

### When to Use YOLO Mode

✅ **Good use cases:**
- Fixing lint errors across multiple files
- Generating boilerplate code
- Initial project setup
- Debugging in readonly mode
- Repetitive refactoring tasks

❌ **Avoid YOLO mode for:**
- Production environments
- Critical system files
- When you need fine control
- Working with sensitive data
- Unfamiliar codebases

### Safety Tips

1. **Always use Docker containers** - Never run YOLO mode directly on your host machine
2. **Use version control** - Commit before starting autonomous sessions
3. **Set time limits** - Check progress every 30 minutes
4. **Review changes** - Examine all modifications before deploying
5. **Start small** - Test with non-critical tasks first

### Monitoring Claude

- Keep terminal visible to see commands being executed
- Check file changes in your IDE's source control view
- Review logs for any errors or unexpected behavior
- Be ready to interrupt if needed (Ctrl+C)

---

## Reference Links

- **Gist with Configuration Changes:** https://gist.github.com/iannuttall/26f43922ed74371284ea8691c5a28902
- **Docker Desktop:** https://docker.com
- **Claude Code Documentation:** https://docs.claude.com/en/docs/claude-code

---

## Notes

- **Container isolation** protects your host machine from potentially harmful commands
- **Port forwarding** must be configured for each port your app uses
- **Authentication persistence** requires proper mount configuration
- **First build** takes longer, subsequent opens are much faster
- Anthropic engineers use this approach for autonomous 30-minute sessions

---

## Quick Reference Commands

```bash
# Clone repository
git clone [repo-url]

# Navigate to folder
cd claude-code

# List all files including hidden
ls -la

# Open in Cursor/VS Code
code .

# Start Claude normally
claude

# Start Claude in YOLO mode
claude --dangerously-skip-permissions

# Open Command Palette
# Mac: Cmd + Shift + P
# Windows/Linux: Ctrl + Shift + P
```

---

**Last Updated:** 2025-10-30
**Status:** ✅ Tested and Working
**Tags:** #claude-code #docker #automation #ai #development #yolo-mode
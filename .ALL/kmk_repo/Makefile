# Directory name where the repository with the upstream is located
REPO_DIR = kmk_firmware

# Branch you want to track from upstream
UPSTREAM_BRANCH = main

# Your local branch name
LOCAL_BRANCH = kmk-main

# Default target (runs by default when you execute `make`)
all:
	@echo "Synchronizing repository with `kmk_firmware` upstream..."
	cd $(REPO_DIR) && \
	git fetch origin $(UPSTREAM_BRANCH) && \
	git checkout -B $(LOCAL_BRANCH) && \
	git merge origin/$(UPSTREAM_BRANCH) && \
	git push origin $(LOCAL_BRANCH)

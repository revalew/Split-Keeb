# Configuring a Submodule as a Separate Branch (`1:1` Copy)

<br/><br/>

Instead of adding a `git submodule` as an object within the main repository (`master`), you can store its contents as a separate branch (`main`).

<br/><br/>

### 1. Clone the Repository (if it already exists)

If the repository already exists, clone it:

```bash
git clone git@github.com:fetch-repo.git
```

<br/><br/>

### 2. Navigate to the Cloned Repository Folder

```bash
cd fetch-repo
```

<br/><br/>

### 3. Check the Submodule Configuration

<br/>

```bash
git remote -v
```

<br/><br/>

> [!INFO]
>
> If the repository was downloaded as a ZIP file, this step will not work.
>
> In that case, proceed to step 4 to initialize a new repository.

<br/><br/>

### 4. (**OPTIONAL**) Initialize an Empty Repository and Add the `fetch` Remote

<br/>

If you do not have an existing repository, initialize a new one:

<br/>

```bash
mkdir fetch-repo && cd fetch-repo
```

<br/>

```bash
git init
```

<br/>

Now, add the `fetch` remote:

<br/>

```bash
git remote add origin git@github.com:fetch-repo.git  # FETCH / PULL ONLY
```

<br/><br/>

### 5. Configure a Different `push` Remote

<br/>

Set a different remote for pushing changes:

<br/>

```bash
git remote set-url origin --push git@github.com:push-repo.git  # PUSH ONLY
```

<br/><br/>

### 6. Verify the Configuration

<br/>

```bash
git remote -v
```

<br/>

Expected Output:

<br/>

```
origin  git@github.com:fetch-repo.git (fetch)
origin  git@github.com:push-repo.git (push)
```

<br/><br/>

### 7. Configure the `Makefile`

<br/>

Set the appropriate variables in the `Makefile`:

<br/>

- `REPO_DIR` – the directory containing the cloned repository,

- `UPSTREAM_BRANCH` – the branch from the `fetch` repository that you want to track,

- `LOCAL_BRANCH` – the branch where the cloned repository will be copied.

<br/>

Example `Makefile`:

<br/>

```make
# Directory name where the repository with the upstream is located
REPO_DIR = fetch-repo

# Branch from upstream repo
UPSTREAM_BRANCH = main

# Your local branch name
LOCAL_BRANCH = kmk-main

# Default target (runs by default when you execute `make`)
all:
	@echo "Synchronizing repository with `fetch-repo` upstream..."
	cd $(REPO_DIR) && \
	git fetch origin $(UPSTREAM_BRANCH) && \
	git checkout -B $(LOCAL_BRANCH) && \
	git merge origin/$(UPSTREAM_BRANCH) && \
	git push origin $(LOCAL_BRANCH)
```

<br/><br/>

### 8. Run the `Makefile`

<br/>

Execute the following command in the directory containing the cloned repository and `Makefile`:

<br/>

```bash
make
```

<br/><br/>

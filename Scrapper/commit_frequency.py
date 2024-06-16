from github import Github
from datetime import datetime, timedelta, timezone

def get_commit_frequency(repo_url, token):
    # Initialize GitHub object with access token
    g = Github(token)

    # Parse repository URL to extract owner and repo name
    owner, repo_name = repo_url.split('/')[-2:]

    # Get the repository object
    repo = g.get_repo(f"{owner}/{repo_name}")

    # Get current date
    current_date = datetime.now(timezone.utc)

    # Calculate start date (two years ago)
    start_date = current_date - timedelta(days=365 * 2)

    # Get all commits from the repository
    commits = repo.get_commits()

    commit_count = 0

    # Count commits within the last two years
    for commit in commits:
        # Convert commit date to offset-aware datetime
        commit_date = commit.commit.author.date.replace(tzinfo=timezone.utc)
        if commit_date >= start_date:
            commit_count += 1

    # Calculate commit frequency
    if commit_count > 0:
        # Calculate the number of days between start_date and current_date
        days_difference = (current_date - start_date).days

        # Calculate commit frequency as commits per day
        commit_frequency = commit_count
        return commit_frequency
    else:
        return 0  # Return 0 if no commits found in the last two years

if __name__ == "__main__":
    # Replace 'YOUR_GITHUB_TOKEN' with your actual GitHub token
    github_token = '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'

    # Replace 'OWNER/REPO_NAME' with the desired GitHub repository
    repository_url = 'https://github.com/microsoft/responsible-ai-toolbox'

    commit_frequency = get_commit_frequency(repository_url, github_token)

    print(f"Commit frequency in the last two years: {commit_frequency:.2f} commits per day")

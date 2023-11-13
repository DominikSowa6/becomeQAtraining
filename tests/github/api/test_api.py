from src.applications.github.api.github_api import GitHubAPIClient


def test_search_for_existing_repo():
    github_api_client = GitHubAPIClient()
    existing_repo_name = 'becomeQAtraining'
    repos = github_api_client.search_repos(existing_repo_name)

    print('Checking total count is not 0')
    assert repos['total_count'] != 0

def test_search_for_nonexisting_repo():
    github_api_client = GitHubAPIClient()
    nonexisting_repo_name = "asdasjdkas"
    repos = github_api_client.search_repos(nonexisting_repo_name)

    print('Checking total count is 0')
    assert repos['total_count'] == 0


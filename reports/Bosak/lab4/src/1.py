import requests
import matplotlib.pyplot as plt
from datetime import datetime, timezone


GITHUB_API = "https://api.github.com/search/repositories"
HEADERS = {"Accept": "application/vnd.github+json", "User-Agent": "Python-Script"}


def search_repos(topic, per_page=100):
    repos = []
    for page in range(1, 6):
        url = f"{GITHUB_API}?q={topic}&sort=stars&order=desc&per_page=20&page={page}"
        response = requests.get(url, headers=HEADERS, timeout=10)
        if response.status_code != 200:
            print(f"Error: {response.status_code}")
            break
        data = response.json()
        repos.extend(data.get("items", []))
        if len(repos) >= per_page:
            break
    return repos[:per_page]


def analyze(repos):
    lang_count = {}
    stars = []
    forks = []
    repo_names = []
    last_updated = []

    for repo in repos:
        lang = repo.get("language")
        if lang:
            lang_count[lang] = lang_count.get(lang, 0) + 1

        stars.append(repo.get("stargazers_count", 0))
        forks.append(repo.get("forks_count", 0))
        date_str = repo["updated_at"]
        date_obj = datetime.fromisoformat(date_str.replace("Z", "+00:00"))
        last_updated.append(date_obj)
        repo_names.append(repo["full_name"])

    total = sum(lang_count.values())
    lang_percent = {k: (v / total) * 100 for k, v in lang_count.items()}

    max_stars_idx = stars.index(max(stars))
    top_repo = repo_names[max_stars_idx]
    top_stars = stars[max_stars_idx]

    avg_forks = sum(forks) / len(forks)

    now = datetime.now(timezone.utc)
    old_count = sum(1 for d in last_updated if (now - d).days > 365)
    old_percent = (old_count / len(last_updated)) * 100

    print("\nMost popular languages:")
    for lang, percent in sorted(lang_percent.items(), key=lambda x: x[1], reverse=True)[:5]:
        print(f"- {lang} ({percent:.1f}%)")

    if len(lang_percent) > 5:
        other = 100 - sum(list(lang_percent.values())[:5])
        print(f"- Other ({other:.1f}%)")

    print(f"\nMost starred repo: \"{top_repo}\" ({top_stars} stars)")
    print(f"Average forks: {avg_forks:.1f}")
    print(f"{old_percent:.0f}% repos not updated in over a year!")

    return lang_percent, stars, repo_names, last_updated


def visualize(lang_percent, stars, repo_names, last_updated, topic):
    langs = list(lang_percent.keys())[:7]
    percents = list(lang_percent.values())[:7]

    plt.figure(figsize=(12, 4))

    plt.subplot(1, 3, 1)
    if sum(percents) > 0:
        plt.pie(percents, labels=langs, autopct="%1.0f%%")
    plt.title("Popular Languages")

    plt.subplot(1, 3, 2)
    top_stars = stars[:10]
    top_names = [n.split("/")[-1][:15] for n in repo_names[:10]]
    plt.barh(top_names[::-1], top_stars[::-1])
    plt.xlabel("Stars")
    plt.title("Top 10 by Stars")

    plt.subplot(1, 3, 3)
    now = datetime.now(timezone.utc)
    days_since = [(now - d).days for d in last_updated[:50]]
    plt.hist(days_since, bins=15, color="orange", edgecolor="black")
    plt.xlabel("Days without updates")
    plt.ylabel("Number of repos")
    plt.title("Last Update Age")

    plt.tight_layout()
    filename = f"{topic.replace(' ', '_')}_analysis.png"
    plt.savefig(filename)
    print(f"\nGraphs saved to \"{filename}\"")
    plt.show()


def main():
    topic = input("Enter topic to analyze: ")
    print(f'Analyzing 100 popular repos on "{topic}"...')

    repos = search_repos(topic)
    if not repos:
        print("No repositories found")
        return

    lang_percent, stars, repo_names, last_updated = analyze(repos)
    visualize(lang_percent, stars, repo_names, last_updated, topic)


if __name__ == "__main__":
    main()
    
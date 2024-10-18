import argparse
import requests
def main():
    parser = argparse.ArgumentParser(description="Fetch LeetCode progress")
    parser.add_argument('username', type=str, help='LeetCode username')
    args = parser.parse_args()

    # Test to check the username input
    print(f"Fetching LeetCode progress for user: {args.username}")






def fetch_leetcode_data(username):
    url = "https://leetcode.com/graphql/"
    query = """
    {
      matchedUser(username: "%s") {
        username
        submitStats {
          acSubmissionNum {
            difficulty
            count
          }
        }
        userCalendar {
          streak
        }
      }
    }
    """ % username

    response = requests.post(url, json={'query': query})
    return response.json()

def main():
    parser = argparse.ArgumentParser(description="Fetch LeetCode progress")
    parser.add_argument('username', type=str, help='LeetCode username')
    args = parser.parse_args()

    data = fetch_leetcode_data(args.username)
    print(f"Data for {args.username}: {data}")



if __name__ == '__main__':
    main()

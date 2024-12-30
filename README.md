# ChatGPT Feedback
ChatGPT Feedback is a simple GitHub action that gets a comment on an issue and update one with the ChatGPT feedback.

## Setup
### Get tokens
You need to obtain [the GitHub PAT (personal access token)](https://github.com/settings/tokens) and [the ChatGPT API key](https://platform.openai.com/api-keys).

The default GitHub token `${{ github.token }}` is not available because the comment you post can only be updated by the current user (you). If you use the default one, you will find the action failed with the message "no comments found for current user".

### Set tokens
You can set the tokens from `https://github.com/<USER>/<REPO>/settings/secrets/actions` with the following keys.

| Description                                                                  | Key               |
| ---------------------------------------------------------------------------- | ----------------- |
| [the GitHub PAT (personal access token)](https://github.com/settings/tokens) | `GH_TOKEN`        |
| [the ChatGPT API key](https://platform.openai.com/api-keys)                  | `CHATGPT_API_KEY` |

### Workflow sample
```yaml
# .github/workflows/chatgpt-feedback.yml

name: ChatGPT Feedback

on:
  issue_comment:
    types: [created]

jobs:
  chatgpt-feedback:
    runs-on: ubuntu-latest
    steps:
      - name: Get a feedback from ChatGPT
        uses: noraworld/chatgpt-feedback@main
        with:
          prompt: "You are a helpful assistant."
          text_before_result: "### Feedback from ChatGPT"
        env:
          GH_TOKEN: ${{ secrets.GH_TOKEN }} # ${{ github.token }} is not sufficient
          CHATGPT_API_KEY: ${{ secrets.CHATGPT_API_KEY }}
```

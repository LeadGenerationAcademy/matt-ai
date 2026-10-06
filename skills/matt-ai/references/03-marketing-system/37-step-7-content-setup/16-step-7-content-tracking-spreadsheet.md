# Step #7: Content Tracking Spreadsheet

Course: Step #7: Content Setup
System: Marketing System
Skool link: https://www.skool.com/leadgenerationacademy/classroom/1df452b8?md=d1c43a97355d45c1be1906cd020f2115

---
Video: this lesson has a video in Skool (about 1:54). Transcript is at the bottom of this file.

Your Content Tracking Spreadsheet will be very similar, and possibly identical, to your Inputs Tracking Spreadsheet.

The purpose is to keep every piece of content from every personal account inside one organized place. It updates automatically once per day so you always know exactly what you have posted and how it is performing.

![image](https://assets.skool.com/f/1d97a8218f0840a8a65c7970ccdf40ce/d30f7b205eed4d7eb93e4a1edf17f11c284090c11815432fb913a3061e1341d8-md.png)

#### Make A Copy

- [Content Tracking Template](https://docs.google.com/spreadsheets/d/1ZFbC_O9zScJQTYxo_l6B2YnIdrFyvWKsid5U4kcj8RE/edit?gid=1694334442#gid=1694334442) [in this skill: assets/templates/content-tracking-template/]

### Links

- [ChatGPT](https://chatgpt.com/)
- [Claude](https://claude.ai/)

### Example

![image](https://assets.skool.com/f/1d97a8218f0840a8a65c7970ccdf40ce/e1ad49362e32440fa475fad59fcf4824d0df0654883d41df9364c3f8ee079de0-md.png)

### Step-by-Step Instructions

1. **Make a copy of the [Content Tracking Template.](https://docs.google.com/spreadsheets/d/1ZFbC_O9zScJQTYxo_l6B2YnIdrFyvWKsid5U4kcj8RE/edit?gid=1694334442#gid=1694334442)** This puts all your content from every personal account in one place, so you can find any post and see how it is performing. [in this skill: assets/templates/content-tracking-template/]
2. **Delete any columns that are irrelevant to your strategy or unavailable on your platforms.** The purpose is to make the Spreadsheet useful, not to fill it with unnecessary metrics because they look impressive.
3. **List every personal account you post from.** This Spreadsheet is for your personal accounts, and company-account tracking can be handled separately if necessary.
4. **List every YouTube channel you run.** Each channel counts as its own account. I have eight YouTube channels connected to mine.
5. **Collect the account ID or URL for every account on that list.** ChatGPT needs the links to everything so the Google Apps Script it writes can pull the content from every account.
6. **Give ChatGPT your tab names, column names, accounts, channels, account IDs, the metrics you want, and the daily update frequency.** Google Apps Script is what works inside Google Sheets, and you do not need to know how to write it. Everybody has different platforms and different things they want tracked, which is why ChatGPT can build yours better than one set of instructions could.
7. **Ask ChatGPT to create the complete Google Apps Script and explain exactly where to paste it.** Tell it to use official platform APIs whenever they are available.
8. **Ask ChatGPT to walk you through each platform individually.** Some platforms require API keys, developer accounts, authorization, or additional permissions, and doing them one at a time keeps it manageable.
9. **Open the Apps Script attached to the Google Sheet.** Follow the exact instructions ChatGPT gave you for where the script goes.
10. **Paste the script in and save it.** This is the complete Google Apps Script ChatGPT created, the one that pulls every post from every account into the Spreadsheet.
11. **Create a time-based trigger that runs the update function once per day.** This is what updates the Spreadsheet automatically once per day, so you always know exactly what you have posted and how it is performing.
12. **Authorize every required permission.** Some platforms need authorization or additional permissions before the script can pull your content. Approve every one ChatGPT walked you through.
13. **Run the script manually once before relying on the automatic trigger.** Do not assume the script works because ChatGPT gave you some code. Run it and check the actual results.
14. **Confirm every connected account appears.** Every personal account you listed should show up, since the whole point is keeping every piece of content in one place.
15. **Confirm every YouTube channel appears.** Go through the list of channels you made and check each one has its own posts in the Spreadsheet.
16. **Confirm new posts are added.** The script should find new content from every platform you post on and add it to the Spreadsheet.
17. **Confirm existing posts are updated.** Existing rows should show each post's latest performance metrics. The script does not need to save a new historical snapshot every day, it only needs to keep the latest numbers updated in the rows already there.
18. **Confirm URLs open the correct content.** The URL is how you find each post again from the Spreadsheet, so it has to open the right one.
19. **Confirm metrics appear in the correct columns.** You are using these numbers to see how every post is performing, so each one needs to be in its correct column.
20. **Confirm no duplicate rows are created.** Every post should appear once. The script should recognize posts already inside the Spreadsheet and update the existing row.
21. **Confirm the daily trigger is active.** The trigger is the only thing keeping this running without you.

### Completion Audit

- Did you make a copy of the Content Tracking Template?
- Did you delete any columns that are irrelevant to your strategy or unavailable on your platforms?
- Did you list every personal account you post from?
- Did you list every YouTube channel you run?
- Did you collect the account ID or URL for every account on that list?
- Did you give ChatGPT your tab names, column names, accounts, channels, account IDs, metrics, and daily update frequency?
- Did you ask ChatGPT to create the complete Google Apps Script and explain exactly where to paste it?
- Did you ask ChatGPT to walk you through each platform individually?
- Did you open the Apps Script attached to the Google Sheet?
- Did you paste the script in and save it?
- Did you create a time-based trigger that runs the update function once per day?
- Did you authorize every required permission?
- Did you run the script manually once before relying on the automatic trigger?
- Did you confirm every connected account appears?
- Did you confirm every YouTube channel appears?
- Did you confirm new posts are added?
- Did you confirm existing posts are updated?
- Did you confirm URLs open the correct content?
- Did you confirm metrics appear in the correct columns?
- Did you confirm no duplicate rows are created?
- Did you confirm the daily trigger is active?

---

## Video Transcript

Automatic captions. Timestamps are minutes:seconds into the video.

[0:00] So this is going to be what I would call an optional step, to be honest, but it's going to track your content. So what you're going to do here is if you want to do this, and I find it very helpful more than as like a form of accountability than anything else, and there's going to have an example here. So what you can do is follow these instructions. So what we're going to do is we're going to ask ChatGbT to write us a Google Apps script, because that's what works in Google Sheets for all of the stuff. We're going to give it our links to everything, and then it's going to basically run a, it's going to create a Google Apps script that basically scrapes everything and puts it in kind

[0:50] of the way that we have it here, right? And then this will basically show you and have all your content in one place so you can find it, you can see it properly. And then it'll also form as an accountability type thing, because if you have stuff posted in here, you are kind of the opposite, usually you don't have stuff posted in here. Then it's mostly like, okay, what the hell is going on type thing. This is also the way that it's inputted into your input tracking spreadsheet. You'd have to be writing a Google script for it. So there's so many different ways to do it. I really can't give you instructions on exactly how to do it. That's why ChatGbT is so much better, because everybody has different platforms.

[1:36] Everybody has different things they want to put in there, and so on. So this is a complete optional step, but I really like to do it so I can see how my posts are performing all in one place. You can also vibe code a dashboard for this if you are obsessed with vibe coding, but having something like this is usually a good thing to have.

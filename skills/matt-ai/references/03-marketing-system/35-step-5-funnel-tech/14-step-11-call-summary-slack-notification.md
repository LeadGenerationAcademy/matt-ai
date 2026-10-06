# Step #11: Call Summary > Slack Notification

Course: Step #5: Funnel Tech
System: Marketing System
Skool link: https://www.skool.com/leadgenerationacademy/classroom/0a453095?md=4d84eae5e11647a690c32ffead493a6c

---
Video: this lesson has a video in Skool (open the Skool link to watch).

Call summary software like Read AI or Fathom automatically records and summarizes your sales calls. This step adds a Slack notification onto the same automation you built in Step #10, so the moment a real call gets summarized, your whole team sees it without anyone opening Read AI or Fathom themselves.

![image](https://assets.skool.com/f/1d97a8218f0840a8a65c7970ccdf40ce/fc5b7491dc014619aec0fe485c1f16ff0c8a6750fa2a4f4eb3a090216a44cf28.png)

### Prerequisites

- [Step #10: Call Summary > Follow Up Flow](https://www.skool.com/leadgenerationacademy/classroom/0a453095?md=bf942b1fff484338a83be3111614d580) (Current Course)

### Links

- [Zapier](https://zapier.com)
- [Slack](https://slack.com)
- [Read AI](https://www.read.ai)

### Framework & Criteria

Paste this message template into your Slack action step's Message Text field. Keep the blank lines, so each section doesn't run into the next one.

Call Completed

Meeting:
Prospect:
Closer:
Start Time:
End Time:

Summary:

Action Items:
1.
2.

Key Questions:
1.
2.

Topics:
1.
2.

For the Formatter steps in Zapier, paste this in as custom text to get a 12-hour format for the call Start Time and End Time:

MMMM D, YYYY h:mm A

### Step-by-Step Instructions

1. **Continue from the Zap you built in [Step #10: Call Summary > Follow Up Flow](https://www.skool.com/leadgenerationacademy/classroom/0a453095?md=bf942b1fff484338a83be3111614d580).** You're not starting over. This step adds onto the end of Path A, right after the "Closed Lost" Add Tag to Subscriber step.
2. **Create a "Call Summary" channel in Slack.** This is where every meeting summary will land, so it needs to exist before you build the Slack step.
3. **Inside Path A, click the + button after the "Closed Lost" Add Tag to Subscriber step to add an action step.** Set Formatter by Zapier as the action app and set the action event to Date / Time. Read AI sends the Start Time and End Time in a format nobody wants to read in Slack. This step turns the Start Time into a normal date and time.
4. **Set the Transform field to Format.**
5. **Insert the Start Time into the Input field.** Click the + button or press "/" and select the call's start time field from Step 1.
6. **Paste MMMM D, YYYY h:mm A into the To Format field as custom text.** Use the format from the Framework & Criteria section above. This gives you a 12-hour time like "September 22, 2026 2:10 PM".
7. **Set the To Timezone field to the timezone you want the call times shown in.**
8. **Click Continue, then click Test step and confirm the Output shows the Start Time in the new format.**
9. **Duplicate the Date / Time step.** Click the three dots on the Date / Time step and select Duplicate. The copy lands right under the original as "Copy: Date / Time in Formatter by Zapier", with every setting already filled in.
10. **In the copy, swap the Start Time in the Input field for the End Time.** Remove Start Time from the Input field, then click the + button or press "/" and select the call's end time field from Step 1. Leave Transform, To Format, and To Timezone exactly as they are.
11. **Click Continue, then click Test step and confirm the Output shows the End Time in the new format.**
12. **Click the + button after the copied Date / Time step to add an action step.** Set Slack as the action app, set the action event to Send Channel Message or Send Private Channel Message, then connect your Slack account. Use Send Channel Message for a public channel and Send Private Channel Message for a private one.
13. **Choose the "Call Summary" channel you created.** This keeps every meeting notification in one place instead of cluttering a channel meant for something else.
14. **Paste the message template into the Message Text field.** Use the template from the Framework & Criteria section above. The fields you insert in the next steps go next to or under each label.
15. **Insert the meeting title after "Meeting:".** Click the + button, or press "/", and select the meeting title field from Step 1. Do not type anything in manually. Typed text won't pull real meeting data.
16. **Insert the prospect's name after "Prospect:".** Select the prospect's name field from Step 1, not the closer's.
17. **Insert the closer's name after "Closer:".** Select the name field for whoever hosted or owned the call from Step 1.
18. **Insert the Output from the first Date / Time step after "Start Time:".** This is the formatted Start Time, not the raw Start Time from Step 1.
19. **Insert the Output from the copied Date / Time step after "End Time:".** This is the formatted End Time, not the raw End Time from Step 1.
20. **Insert the Summary field on the line under "Summary:".** The label goes on its own line here since the summary itself can run long.
21. **Insert the action items on their own lines under "Action Items:".** Insert the first action item after "1.", the second after "2.", and so on for however many action items your call summary software gives you.
22. **Insert the key questions on their own lines under "Key Questions:".** Same process as the action items, one key question per line.
23. **Insert the topics on their own lines under "Topics:".** Same process again, one topic per line. This is the last section of the message.
24. **Scroll to the bottom without changing anything else, then confirm Send Channel Message is set to Yes.** Every other field can stay at its default setting. This is what actually allows the message to send.
25. **Click Continue, then click Test step and check whether the message arrived in the correct Slack channel with every field filled in.** Confirm every label has its matching data next to it, the times show in the new format, and nothing came through blank.
26. **Continue to [Step #12: Call Summary > Winback Flow](https://www.skool.com/leadgenerationacademy/classroom/0a453095?md=0b55d0b2480449399dccb11464e780ed) to keep building this automation.** Don't publish yet. You'll publish the whole Zap once at the end of Step #13.

### Completion Audit

- Did you continue from the Zap you built in Step #10?
- Did you create a "Call Summary" channel in Slack?
- Did you add a Formatter by Zapier step inside Path A after the "Closed Lost" tag step, with Date / Time as the action event?
- Did you set the Transform field to Format?
- Did you insert the Start Time into the Input field?
- Did you paste MMMM D, YYYY h:mm A into the To Format field?
- Did you set the To Timezone field?
- Did you test the step and confirm the Start Time came out in the new format?
- Did you duplicate the Date / Time step?
- Did you swap the Start Time in the copy's Input field for the End Time?
- Did you test the copy and confirm the End Time came out in the new format?
- Did you add a Slack action step after the copied Date / Time step, set the action event, and connect your Slack account?
- Did you choose the "Call Summary" channel you created?
- Did you paste the message template into the Message Text field?
- Did you insert the meeting title after "Meeting:"?
- Did you insert the prospect's name after "Prospect:"?
- Did you insert the closer's name after "Closer:"?
- Did you insert the first Date / Time Output after "Start Time:"?
- Did you insert the copied Date / Time Output after "End Time:"?
- Did you insert the Summary field under "Summary:"?
- Did you insert the action items on their own lines?
- Did you insert the key questions on their own lines?
- Did you insert the topics on their own lines?
- Did you scroll to the bottom and confirm Send Channel Message is set to Yes?
- Did you click Test step and check whether the message arrived with every field filled in?
- Did you continue to Step #12: Call Summary > Winback Flow?

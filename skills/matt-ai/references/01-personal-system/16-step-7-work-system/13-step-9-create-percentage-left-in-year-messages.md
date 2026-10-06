# Step #9: Create Percentage-Left-In-Year Messages

Course: Step #7: Work System
System: Personal System
Skool link: https://www.skool.com/leadgenerationacademy/classroom/5c9acee6?md=1a51a3410ec14bb89a574bf268c44dc5

---
![image](https://assets.skool.com/f/1d97a8218f0840a8a65c7970ccdf40ce/2659f19e12274ffdbc981921da427dc0453786c30e5240f0ad4328d6435a6deb-md.png)

### Prerequisites

- [Step #6: Create Accountability Notifications](https://www.skool.com/leadgenerationacademy/classroom/5c9acee6?md=6bd8d702582e4d3e916491f1feb86f73) (Current Course)

### Template

- [Percentage Left In The Year Zapier Code](https://docs.google.com/document/d/1Ruqq0ZmttIuDjqxguaz0bZrhme6yDbgxSQiaavRCOik/edit?usp=sharing) [in this skill: assets/templates/percentage-left-in-the-year-zapier-code/]

### Step-by-Step Instructions

1. **Set the trigger app to Schedule by Zapier and the trigger event to "Every Day."** Nothing starts this automation except the time of day, there's no form or submission behind it.
2. **Set the Time of Day to 15 to 30 minutes before you normally wake up.** The message should already be sitting there when you pick up your phone, not arriving while you're mid morning routine.
3. **Set "Trigger on weekends" to "Yes."** There's also an optional Timezone Override field on this screen. Only touch it if your Zapier account is set to a different timezone than the one you actually live in.
4. **Test the trigger.** You need a successful trigger on file before you can build anything on top of it.
5. **Add an action step and set the action app to Code by Zapier.** This is the step that works out the percentage.
6. **Set the action event to "Run Javascript."** Code by Zapier also offers Python. The code in the document is written in Javascript, so this is the one you want.
7. **Set the code language to JavaScript.** Zapier usually drops you straight into the code editor, so check the language dropdown at the top before you touch anything else.
8. **Delete the placeholder code already in the editor.** Zapier pre-fills the editor with example code. Clear all of it out, otherwise you end up running both sets at once.
9. **Paste in the code from the [Percentage Left In The Year Zapier Code](https://docs.google.com/document/d/1Ruqq0ZmttIuDjqxguaz0bZrhme6yDbgxSQiaavRCOik/edit?usp=sharing).** Paste it exactly as written in the document, don't edit any of it. The text you paste into Gmail and SMS later references this code directly, so changing it breaks the rest of the build. [in this skill: assets/templates/percentage-left-in-the-year-zapier-code/]
10. **Press Run Code.** You have to do this before continuing. It confirms the calculation works and produces the four values the next steps use, Percent Gone, Year, Days Elapsed and Days Remaining.
11. **Add an action step and set the action app to Gmail.** This is what sends the email version of the message.
12. **Connect your account.** This authorizes the automation platform to send email on your behalf.
13. **Set the action event to "Send Email."** Gmail offers several events here. Send Email is the one that composes a new message rather than replying to an existing thread.
14. **Enter your own email address in the To field.** This message is only going to you, nobody else needs it.
15. **Paste the Subject text from the document into the Subject field.** Copy it straight from the document, no editing needed. If you'd rather word it differently, change the sentence around the numbers but leave everything inside the curly brackets exactly as it is.
16. **Paste the Body text from the document into the Body field.** Same as the subject. Every other field on this screen can be left on its default.
17. **Test the action step.** This sends a real email using the numbers from your code step.
18. **Check your inbox to confirm the email sent correctly with the right numbers.** If the numbers are missing or the brackets show up as plain text, the code step didn't run properly. Go back and press Run Code.
19. **Add an action step and set the action app to SMS by Zapier.** This sends the same message to your phone.
20. **Connect your phone number.** If SMS is unavailable where you are, use the messaging app you reliably check every morning instead. T-Mobile numbers in particular are not supported by SMS by Zapier.
21. **Set the action event to "Send SMS."** This is the one that sends a plain text message to the number you just connected.
22. **Set the From Number to a specific number instead of "Random."** Picking one number means every message lands in the same thread instead of starting a new one every day.
23. **Paste the Message text from the document into the Message field.** Same content as the email body, formatted for a text message.
24. **Test the action step.** This sends a real text using the numbers from your code step.
25. **Check your phone to confirm the text sent correctly with the right numbers.** Same check as the email.
26. **If it works, publish the automation. If not, ask ChatGPT or Claude to diagnose the problem.** Only publish once you've confirmed both the email and the text actually arrive with the correct numbers.

### Completion Audit

- Did you set the trigger app to Schedule by Zapier and the trigger event to "Every Day"?
- Did you set the Time of Day to 15 to 30 minutes before you normally wake up?
- Did you set "Trigger on weekends" to "Yes"?
- Did you test the trigger?
- Did you add an action step and set the action app to Code by Zapier?
- Did you set the action event to "Run Javascript"?
- Did you set the code language to JavaScript?
- Did you delete the placeholder code already in the editor?
- Did you paste in the code from the Percentage Left In The Year Zapier Code?
- Did you press Run Code?
- Did you add an action step and set the action app to Gmail?
- Did you connect your account?
- Did you set the action event to "Send Email"?
- Did you enter your own email address in the To field?
- Did you paste the Subject text from the document into the Subject field?
- Did you paste the Body text from the document into the Body field?
- Did you test the action step?
- Did you check your inbox to confirm the email sent correctly with the right numbers?
- Did you add an action step and set the action app to SMS by Zapier?
- Did you connect your phone number?
- Did you set the action event to "Send SMS"?
- Did you set the From Number to a specific number instead of "Random"?
- Did you paste the Message text from the document into the Message field?
- Did you test the action step?
- Did you check your phone to confirm the text sent correctly with the right numbers?
- Did you publish the automation only after confirming everything works?

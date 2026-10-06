# Step #12: Call Summary > Winback Flow

Course: Step #5: Funnel Tech
System: Marketing System
Skool link: https://www.skool.com/leadgenerationacademy/classroom/0a453095?md=0b55d0b2480449399dccb11464e780ed

---
Video: this lesson has a video in Skool (open the Skool link to watch).

Continuing off the same automation, prospects who go Closed Lost also get added to a 90 day, 180 day, and 365 day winback sequence, on top of the Follow Up Flow from Step #10. None of this undoes itself, if they pay before one of these sequences finishes, you have to pull them out manually.

![image](https://assets.skool.com/f/1d97a8218f0840a8a65c7970ccdf40ce/f0aa9110914344b38b6f5d458c4921d01787f0e7d2284d23ba480f4d89ba6447.png)

### Prerequisites

- [Step #11A: 90 Day Winback Flow](https://www.skool.com/leadgenerationacademy/classroom/ff36840f?md=aee0e15afb6044ff9f0bd585e8965856) (Funnel Emails Course)
- [Step #12A: 180 Day Winback Flow](https://www.skool.com/leadgenerationacademy/classroom/ff36840f?md=7cd8b49a45d1414592d1b01cc59ec238) (Funnel Emails Course)
- [Step #13A: 365 Day Winback Flow](https://www.skool.com/leadgenerationacademy/classroom/ff36840f?md=b5b74b411c94404ebf78d75d20cdfe38) (Funnel Emails Course)
- [Step #10: Call Summary > Follow Up Flow](https://www.skool.com/leadgenerationacademy/classroom/0a453095?md=bf942b1fff484338a83be3111614d580) (Current Course)
- [Step #11: Call Summary > Slack Notification](https://www.skool.com/leadgenerationacademy/classroom/0a453095?md=4d84eae5e11647a690c32ffead493a6c) (Current Course)

### Links

- [Zapier](https://zapier.com)
- [Kit](https://kit.com/)

### Step-by-Step Instructions

1. **Continue from the Zap you built in [Step #11: Call Summary > Slack Notification](https://www.skool.com/leadgenerationacademy/classroom/0a453095?md=4d84eae5e11647a690c32ffead493a6c).** You're adding onto the end of Path A, right after the Slack step.
2. **Create a "90 Day Winback", "180 Day Winback", and "365 Day Winback" tag in your email platform.** Each tag starts its own sequence, so all three need to exist before the automations watching for them do.
3. **Create a new automation triggered by the "90 Day Winback" tag that enrolls the subscriber into your 90 day sequence, then confirm it's set to Active.** An automation left inactive won't enroll anyone, even if the tag gets added correctly from Zapier.
4. **Create a new automation triggered by the "180 Day Winback" tag that enrolls the subscriber into your 180 day sequence, then confirm it's set to Active.** Three tags means three automations, and all three need to be Active on their own.
5. **Create a new automation triggered by the "365 Day Winback" tag that enrolls the subscriber into your 365 day sequence, then confirm it's set to Active.** Last of the three. Check it the same way you checked the other two.
6. **Set a delay on the first email of each winback sequence: 90 days for the "90 Day Winback" sequence, 180 days for the "180 Day Winback" sequence, and 365 days for the "365 Day Winback" sequence.** Without the delay, all three winback sequences start sending the same day as the "Closed Lost" tag.
7. **Inside Path A, click the + button after the Slack step to add an action step.** Set your email platform as the action app, set the action event to Add Tag to Subscriber, then connect your account if you haven't already. This keeps the winback tags tied to the same real call summaries as everything else in this path.
8. **Set the Tag field to "90 Day Winback".** This has to match the exact tag your automation from step 3 is watching for.
9. **Insert the participant's Email, First Name, and Last Name into the Email, First Name, and Last Name fields, not the call owner's.** Click the + button or press "/" and insert the prospect's email, first name, and last name fields from Step 1. Don't type them in manually, and don't map the owner's details by mistake.
10. **Click Continue, then click Test step and confirm the "90 Day Winback" tag applied.** Test this one before duplicating it, so the two copies are built off a step you already know works.
11. **Duplicate the "90 Day Winback" step.** Click the three dots on the step and select Duplicate. The copy lands right under the original with the Email, First Name, and Last Name already filled in.
12. **In the copy, change the Tag field to "180 Day Winback".** Leave Email, First Name, and Last Name exactly as they are. This has to match the exact tag your automation from step 4 is watching for.
13. **Duplicate the "180 Day Winback" step.** Same as before, click the three dots on the step and select Duplicate.
14. **In the new copy, change the Tag field to "365 Day Winback".** Leave Email, First Name, and Last Name exactly as they are. This has to match the exact tag your automation from step 5 is watching for.
15. **Test all three Add Tag to Subscriber steps.** Confirm each of the three tags actually applies from the same test record you've been using through this whole path.
16. **Check your email platform to confirm all three tags were added and the test subscriber was enrolled in all three winback sequences.** Because of the 90, 180, and 365 day delays on the first emails, no winback emails will send during testing. Open each winback automation and confirm it shows the test subscriber. Three sequences means three separate things to verify. Don't assume one working means all three did.
17. **If the prospect pays, update their opportunity status to "Closed Won" in your CRM, then open their subscriber profile in your email platform and remove them from every sequence they're in.** Nothing in this automation knows when someone pays, so this part is on you or your team. If you don't pull them out, they keep getting Follow Up and winback emails after they're already a client.
18. **Continue to [Step #13: No Call Summary > No Show Flow](https://www.skool.com/leadgenerationacademy/classroom/0a453095?md=d40812de91b64fd88b32f743dd94febb) to finish building this automation.** Don't publish yet. You'll publish the whole Zap once at the end of Step #13.

### Completion Audit

- Did you continue from the Zap you built in Step #11?
- Did you create a "90 Day Winback", "180 Day Winback", and "365 Day Winback" tag in your email platform?
- Did you create and activate the automation triggered by the "90 Day Winback" tag?
- Did you create and activate the automation triggered by the "180 Day Winback" tag?
- Did you create and activate the automation triggered by the "365 Day Winback" tag?
- Did you set a 90, 180, and 365 day delay on the first email of each winback sequence?
- Did you add an action step inside Path A after the Slack step, with Add Tag to Subscriber as the action event?
- Did you set the Tag field to "90 Day Winback"?
- Did you insert the participant's Email, First Name, and Last Name, not the call owner's?
- Did you test the "90 Day Winback" step before duplicating it?
- Did you duplicate the "90 Day Winback" step?
- Did you change the copy's Tag field to "180 Day Winback"?
- Did you duplicate the "180 Day Winback" step?
- Did you change the new copy's Tag field to "365 Day Winback"?
- Did you test all three Add Tag to Subscriber steps?
- Did you confirm all three tags were added and the test subscriber was enrolled in all three winback sequences?
- Did you update the opportunity status to "Closed Won" and remove anyone who pays from every sequence they're in?
- Did you continue to Step #13: No Call Summary > No Show Flow?

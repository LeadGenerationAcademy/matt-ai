# Step #13: No Call Summary > No Show Flow

Course: Step #5: Funnel Tech
System: Marketing System
Skool link: https://www.skool.com/leadgenerationacademy/classroom/0a453095?md=d40812de91b64fd88b32f743dd94febb

---
Video: this lesson has a video in Skool (open the Skool link to watch).

Call summary software like Read AI or Fathom writes "No summary available due to limited meeting data" when a call didn't actually happen the way it should have, no show, dropped call, whatever the reason.

Continuing off the same automation from Step #10, this step catches that exact case and moves that lead to "No Show" in your CRM, then into a No Show Flow in your email platform instead of Closed Lost.

![image](https://assets.skool.com/f/1d97a8218f0840a8a65c7970ccdf40ce/b1c6fd1297c4411da5dd05961238c1e1d002e721b45d46598f1a65ff3fcf7856.png)

### Prerequisites

- [Step #9A: No Show Flow](https://www.skool.com/leadgenerationacademy/classroom/ff36840f?md=65979b6ded20449e824f1c461e73b976) (Funnel Emails Course)
- [Step #10: Call Summary > Follow Up Flow](https://www.skool.com/leadgenerationacademy/classroom/0a453095?md=bf942b1fff484338a83be3111614d580) (Current Course)
- [Step #12: Call Summary > Winback Flow](https://www.skool.com/leadgenerationacademy/classroom/0a453095?md=0b55d0b2480449399dccb11464e780ed) (Current Course)

### Links

- [Zapier](https://zapier.com)
- [Close](https://www.close.com)
- [Kit](https://kit.com)

### Step-by-Step Instructions

1. **Continue from the Zap you built in [Step #12: Call Summary > Winback Flow](https://www.skool.com/leadgenerationacademy/classroom/0a453095?md=0b55d0b2480449399dccb11464e780ed).** You're not starting over. Find Lead and Find Opportunities already run for every call before the split. You're only building inside Path B here.
2. **Create a "No Show" tag in your email platform.** This tag is what starts your No Show Flow, so it needs to exist before you build anything else.
3. **Create a new automation inside your email platform, set the trigger to Tag Is Added, then select the "No Show" tag.** This has to match exactly. It's the same tag Zapier applies later in this build.
4. **Add an action step to enroll the subscriber into your No Show Flow, then confirm the automation is set to Active.** An automation left inactive will not enroll anyone, even if it's built correctly.
5. **Create a Rule in your email platform that removes the subscriber from the No Show Flow sequence when the "Closed Lost" tag is added.** In Kit, go to Automations, then Rules, set the trigger to Tag Added with the "Closed Lost" tag, and set the action to Unsubscribe from Sequence with your No Show Flow sequence. Someone can no-show, rebook, then complete a call. Without this Rule, they get the Follow Up Flow and the No Show Flow at the same time.
6. **Inside Path B, set the condition so it only continues when the Summary field does not exist.** Set the rule type to Custom rules. Click Choose field and select the summary field from Step 1 under Previous Steps. Click Choose condition and select Does not exist. This is the opposite of Path A, which only continues when the Summary field exists.
7. **Click the + button to add an action step.** Set Close as the action app, set the action event to Update Opportunity, then connect your account if you haven't already.
8. **Insert the ID from Step 3 into the Opportunity ID field.** Click into the Opportunity ID field, click the + button or press "/" to open Insert Data, go to Previous Steps, and select ID from Step 3 (Find Opportunities in Close).
9. **Set the Status dropdown to "No Show".** Leave Assigned to User, Contact ID, Confidence, and every other field blank.
10. **Click the + button to add an action step.** Set your email platform as the action app, set the action event to Add Tag to Subscriber, then connect your account if you haven't already. This is the specific action that enrolls the subscriber into the email platform automation you built in step 3.
11. **Set the Tag field to "No Show".** This has to match the exact tag your email platform automation is watching for.
12. **Insert the participant's Email, First Name, and Last Name into the Email, First Name, and Last Name fields, not the call owner's.** Click the + button or press "/" and insert the prospect's email, first name, and last name fields from Step 1. Don't type them in manually. This needs to be the actual person who was supposed to be on the call.
13. **Test every step you just built in this path.** Confirm the opportunity status updates and the tag applies correctly, both from the same test record.
14. **Check your CRM and your email platform to confirm the opportunity status and tag both updated correctly from the test.** Two systems are getting updated here, and it's easy to confirm one and assume the other worked.
15. **Confirm the No Show Flow sequence actually started sending.** This proves the tag correctly triggered the automation you built inside your email platform, proving the whole chain works end to end.
16. **If it works, publish the automation.** If not, ask ChatGPT or Claude to diagnose the problem. You're publishing the whole Zap from Steps #10 through #13 at once, so don't publish until both Path A and Path B have been confirmed working end to end.

### Completion Audit

- Did you continue from the Zap you built in Step #12?
- Did you create a "No Show" tag in your email platform?
- Did you create a new automation inside your email platform, set the trigger to Tag Is Added, and select the "No Show" tag?
- Did you add an action step to enroll the subscriber into your No Show Flow and confirm the automation is set to Active?
- Did you create a Rule that removes the subscriber from the No Show Flow sequence when the "Closed Lost" tag is added?
- Did you set Path B's condition to only continue when the Summary field does not exist?
- Did you add an action step, set Close as the action app, set the action event to Update Opportunity, and connect your account?
- Did you insert the ID from Step 3 into the Opportunity ID field?
- Did you set the Status to "No Show"?
- Did you add an action step, set your email platform as the action app, set the action event to Add Tag to Subscriber, and connect your account?
- Did you set the Tag field to "No Show"?
- Did you insert the participant's Email, First Name, and Last Name, not the call owner's?
- Did you test every step in this path?
- Did you confirm your CRM and your email platform both updated correctly from the test?
- Did you confirm the No Show Flow sequence actually started sending?
- Did you publish the automation, or diagnose the problem if it didn't work?

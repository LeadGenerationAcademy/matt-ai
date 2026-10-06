# Step #5: Application/Opt In > Welcome Flow

Course: Step #5: Funnel Tech
System: Marketing System
Skool link: https://www.skool.com/leadgenerationacademy/classroom/0a453095?md=48cd18e8f0804422ab98e6e7bf43ec85

---
Video: this lesson has a video in Skool (open the Skool link to watch).

Once someone opts in or applies to your form, you want them tagged and automatically dropped into your Welcome Flow email sequence, without anyone manually adding them.

![image](https://assets.skool.com/f/1d97a8218f0840a8a65c7970ccdf40ce/9036dad3f64e432bbfdd1657836d9669cd05d2b90e004eb69b9c0288e501514f.png)

### Prerequisites

- [Step #1: Opt In Page](https://www.skool.com/leadgenerationacademy/classroom/94f7e3ec?md=7063959ac1fe4a32b1fa9a2de80315fc) (Funnel Pages Course)
- [Step #4A: Application Form](https://www.skool.com/leadgenerationacademy/classroom/94f7e3ec?md=ef780cefa17b4c27b6e83db128999d5c) (Funnel Pages Course)
- [Step #5A: Welcome Flow](https://www.skool.com/leadgenerationacademy/classroom/ff36840f?md=f61ef3a01fe74f08a9919594b977c394) (Funnel Emails Course)

### Links

- [Zapier](https://zapier.com)
- [Kit](https://kit.com/)

### Step-by-Step Instructions

1. **Create an "Opt In" tag and a tag for each Lead Magnet in your email platform.** These tags are what start your Welcome Flow, so they need to exist before you build anything else. If you've already created them, you can skip this step and use the ones you have.
2. **Create a new automation inside your email platform, set the trigger to Tag Is Added, then select the specific Lead Magnet tag.** Choosing the general "Opt In" tag instead would enroll every opt-in into the same Welcome Flow regardless of which lead magnet they requested.
3. **Add an action step to enroll the subscriber into your finished Welcome Flow, then confirm the automation is set to Active.** Make sure you're selecting the completed sequence, not a blank or placeholder one. An automation left inactive will not enroll anyone, even if it's built correctly.
4. **If your form connects natively to your email platform, skip to step 11.** Some email platforms let you build the opt-in form directly inside the platform itself. In that case the tag gets applied natively and you don't need Zapier at all.
5. **If your form does not connect natively, log in to [Zapier](https://zapier.com), then click Create, then click Zaps.** Sign up if you don't already have an account. This is where you'll connect your form to your email platform.
6. **Set your opt-in or application platform as the trigger app, set the trigger event to New Form Submission, then connect your account.** Use whichever platform your opt-in or application form was actually built on. Every app used in a Zap needs its own account connection before you can configure it.
7. **Click the + button to add an action step. Set your email platform as the action app, set the action event to Add Tag to Subscriber, then connect your account if you haven't already.** This is the specific action that enrolls the subscriber into the email platform automation you built in step 2.
8. **Select the specific Lead Magnet tag in the Tag field.** This has to match the exact tag your email platform automation is watching for.
9. **Insert the Email and First Name fields from your tested form submission.** Click into each field, then click the + button or press "/" to insert the actual Email and First Name from the form response you already tested. Do not type these in manually. Typed text won't pull real submission data.
10. **Click Continue, then click Test step and check your email platform to confirm the tag was added to the test subscriber.** This confirms the Zapier side actually worked.
11. **Confirm the Welcome Flow sequence actually started sending.** This confirms the tag correctly triggered the automation you built inside your email platform, proving the whole chain works end to end.
12. **If everything works, publish the automation. If not, ask ChatGPT or Claude to diagnose the problem.** Don't publish a Zap that hasn't been confirmed working end to end. Either confirm every check above passed or get the failure diagnosed first.

### Completion Audit

- Did you create an "Opt In" tag and a tag for each Lead Magnet in your email platform, or confirm you already have them?
- Did you create a new automation inside your email platform, set the trigger to Tag Is Added, and select the specific Lead Magnet tag?
- Did you add an action step to enroll the subscriber into your finished Welcome Flow and confirm the automation is set to Active?
- If your form connects natively to your email platform, did you skip to step 11?
- If your form does not connect natively, did you log in to Zapier, then click Create, then click Zaps?
- Did you set your opt-in or application platform as the trigger app, set the trigger event to New Form Submission, and connect your account?
- Did you add an action step, set your email platform as the action app, set the action event to Add Tag to Subscriber, and connect your account?
- Did you select the specific Lead Magnet tag in the Tag field?
- Did you insert the Email and First Name fields from your tested form submission?
- Did you click Test step and check your email platform to confirm the tag was added to the test subscriber?
- Did you confirm the Welcome Flow sequence actually started sending?
- Did you publish the automation, or diagnose the problem if something didn't work?

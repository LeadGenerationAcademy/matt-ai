# Step #0B: Email/Domain Setup

Course: Step #3: Funnel Emails
System: Marketing System
Skool link: https://www.skool.com/leadgenerationacademy/classroom/ff36840f?md=5771a68303414582a4ecdcedba83ac90

---
Video: this lesson has a video in Skool (about 2:53). Transcript is at the bottom of this file.

Your Funnel Emails should be sent using your company domain. These emails are part of your Sales Process. Your newsletter is closer to regular content and should normally be sent using your personal domain.

![image](https://assets.skool.com/f/1d97a8218f0840a8a65c7970ccdf40ce/097abc065e1240ef884a102215e07203f9b27664b1964c36809ff15f95fb28e7.png)

### Prerequisites

- [Step #0A: Platform Setup](https://www.skool.com/leadgenerationacademy/classroom/ff36840f?md=9b9fcb9c1cf0431fae1cad256d8f8fdc) (Current Course)

### Framework

1. Create a dedicated sending domain
2. Separate Funnel Email from your newsletter
3. Configure SPF
4. Configure DKIM
5. Configure DMARC
6. Use a real sending address
7. Connect the domain to your platform

### Step-by-Step Instructions

1. **Create A Dedicated Sending Subdomain Using Your Company Domain.** For example, [email.company.com](http://email.company.com). This keeps your automated Funnel Emails separate from your normal employee inboxes while still using your company identity.
2. **Connect The Subdomain Inside Your Email Platform.** Your Email Platform should walk you through this process; it's a separate step from creating the subdomain itself since the subdomain has to exist first before the platform can verify and connect to it.
3. **Route Funnel Emails Through Your Company Sending Domain.** This includes Lead Magnet Delivery, Welcome Flow, Application Abandonment, Pre-Call Flow, No-Show Flow, and Post-Call Follow-Up. All of these are part of your Sales Process, which is why they use your company identity.
4. **Route Your Newsletter Through Your Personal Domain.** For example, Funnel Emails on [email.company.com](http://email.company.com) and Newsletter on [yourname.com](http://yourname.com). Your Newsletter is closer to regular content, not your Sales Process, so it should normally live on a separate domain from your Funnel Emails.
5. **Add The SPF Record Your Email Platform Provides.** SPF tells inbox providers which platforms are allowed to send Email for your domain. Copy the record exactly and do not create multiple conflicting SPF records, since conflicting records can cause authentication to fail entirely.
6. **Add Every DKIM Record Your Email Platform Provides And Verify Them.** DKIM adds a signature that lets inbox providers verify the Email was genuinely sent through your authorized Email Platform. Your platform may give you more than one DKIM record, so add and verify all of them, not just the first one.
7. **Add The DMARC Record Your Email Platform Recommends.** DMARC tells inbox providers what to do when an Email fails SPF or DKIM. It also lets you monitor whether unauthorized systems are attempting to send Email using your domain.
8. **Send From A Real Address That Can Receive Replies.** For example, [matthew@company.com](mailto:matthew@company.com). Never use a no-reply address; replies are part of the Deliverability Flywheel and should reach an inbox someone monitors.
9. **Confirm Your Email Platform Shows The Domain As Verified.** This is the platform-side confirmation that everything above was set up correctly, separate from the DNS-level checks that follow.
10. **Confirm SPF, DKIM, And DMARC All Pass.** Check all three individually, since it's possible for one to pass while another still fails or is misconfigured.
11. **Confirm Replies Reach The Correct Inbox.** Reply to a test send from this new domain and make sure it lands somewhere a real person monitors, not a dead inbox.
12. **Confirm Unsubscribe Handling Works.** Test that clicking unsubscribe actually removes the contact so you're not sending to people who opted out.
13. **Start Sending Only To People Actively Entering Your Funnel.** Do not immediately blast a massive list from a brand-new Sending Domain; increase volume naturally as the domain builds a sending reputation.

### Completion Audit

- Did you create a dedicated sending subdomain using your company domain?
- Did you connect the subdomain inside your Email Platform?
- Are your Funnel Emails routed through your company Sending Domain?
- Is your Newsletter routed through your personal domain?
- Did you add the SPF record your Email Platform provided?
- Did you add and verify every DKIM record your Email Platform provided?
- Did you add the DMARC record your Email Platform recommended?
- Are you sending from a real address that can receive replies?
- Does your Email Platform show the domain as verified?
- Do SPF, DKIM, and DMARC all pass?
- Do replies reach the correct inbox?
- Does unsubscribe handling work?
- Are you starting by sending only to people actively entering your Funnel?

---

## Video Transcript

Automatic captions. Timestamps are minutes:seconds into the video.

[0:00] As far as your email domain setup go and for your SMS, for SMS, you're going to need to apply for an A2P10DC. It's very easy on Rosen, but for your email, of course, I would hope so that your email matches your domain, but we really need to, whenever we do this essentially, like whenever we set up our email tool, like I just say it was Kit, we need to make sure that we use a dedicated sending subdomain for it. And it should be, like these step-by-step instructions kind of make it sound more complicated than it actually is, but it's like go to where it says dedicated sending domain inside

[0:46] that platform and set it up. Basically, all you have to do is put a bunch of DNS records to your domain and it should work. And then, basically, it will warm itself up over the course of a week, two weeks, three weeks, until it's like maximum warm. And then you should definitely see a ton, like, much better increase in your deliverability. So basically, if you don't know what it is, SPF records, DMARC records, DKIM records, you got to make sure all of those are in there or is your email deliverability is going to be absolutely busted. I also would prefer, because we're going to do a newsletter as part of our content strategy, I would prefer our newsletter to be on a separate domain, like you could either set that

[1:33] from your own personal domain, like I send my newsletter from MatthewBLarson.com or I'll send it from the leadgenerationnewsletter.com, like either one, whereas my, so like my main domain that my flows and stuff come from, leadgenerationacademy.ai. My personal gobs from MatthewBLarson.com, and I set them up like that separate for a few reasons. Number one, your newsletter will usually get better open click rates, all that kind of stuff, then your actual sales, you flow emails, and having them separate will tank your newsletter deliverability and having them in the same thing. So that's one. And then every time someone signs it for one, they're automatically signed up for the other. And then they'd have to unsubscribe separately. So I got them over time, you know what I mean? And I guess a third reason, especially if you don't do it on your own domain, like a newsletter

[2:24] can be worth a lot of money if you really hit it big, and you can sell your newsletter in business and get sponsors for it independently of your actual business, which would not be the case if you have it on your main domain. So make sure you're dedicated setting domain is up. Make sure you have all of this up and make sure you get a separate newsletter domain. If you don't really care about all that stuff, just get your own name, you should be getting your own name anyways as your domain. So it's just one of those things where it's just more setup.

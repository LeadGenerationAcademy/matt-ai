# Step #2: Installing The Pixel

Course: Step #8: Paid Ads Setup
System: Marketing System
Skool link: https://www.skool.com/leadgenerationacademy/classroom/c0a462fb?md=27ec205cd1974f08be8b7c354515f350

---
Video: this lesson has a video in Skool (about 2:25). Transcript is at the bottom of this file.

![image](https://assets.skool.com/f/1d97a8218f0840a8a65c7970ccdf40ce/a061a6b2ae9d4a3185dd2d4c2d6ecc31accbd63cea6e4982a3994e0af8b0a4fb.png)

### Prerequisites

- [Step #1: Opt In Page](https://www.skool.com/leadgenerationacademy/classroom/94f7e3ec?md=7063959ac1fe4a32b1fa9a2de80315fc) (Funnel Pages Course)
- [Step #2: Opt In Confirmation Page](https://www.skool.com/leadgenerationacademy/classroom/94f7e3ec?md=cf002f544ab846f88aa372a80d57aa76) (Funnel Pages Course)
- [Step #3A: Sales Page Above The Fold](https://www.skool.com/leadgenerationacademy/classroom/94f7e3ec?md=3feb286fb88041009e34f24ca2d7789c) (Funnel Pages Course)
- [Step #3B: Rest Of Sales Page](https://www.skool.com/leadgenerationacademy/classroom/94f7e3ec?md=3b6742b4d7514d09aea0a756f39f0cf0) (Funnel Pages Course)
- [Step #4A: Application Form](https://www.skool.com/leadgenerationacademy/classroom/94f7e3ec?md=ef780cefa17b4c27b6e83db128999d5c) (Funnel Pages Course)
- [Step #4B: Call Booked Page](https://www.skool.com/leadgenerationacademy/classroom/94f7e3ec?md=6ca6b510654b459e82772aade2c1881f) (Funnel Pages Course)
- [Step #5: Call Booked Confirmation Page](https://www.skool.com/leadgenerationacademy/classroom/94f7e3ec?md=c1c3747425614c5596ed450c09f645d3) (Funnel Pages Course)
- [Step #1: Setup Meta Ads](https://www.skool.com/leadgenerationacademy/classroom/c0a462fb?md=578291ccdd0a4151a19948a3acc6fba3) (Current Course)

### Install

- [Meta Ads Data Advisor](https://chromewebstore.google.com/detail/meta-ads-data-advisor/fdgfkebogiimcoedlicjlajpkdmockpc?hl=en)

### Links

- [Events Manager](https://eventsmanager.facebook.com/events_manager2) (In Facebook Business Manager)
- [Webflow](https://webflow.com/)

### Step-by-Step Instructions

1. **Open [Events Manager](https://eventsmanager.facebook.com/events_manager2).** You can also get here by opening your Business Manager and clicking "Events Manager" in the left navigation bar. This is where your pixel and everything it collects is managed.
2. **Click "Datasets".** This gives you every pixel sitting inside your Business Manager.
3. **Select the pixel you want to use.** You will most likely only have one. If you have multiple, choose the one you should already have made and connected in the previous step.
4. **Click "Set up Meta Pixel".** This sits under "Gather website events from browser activity" on the dataset overview screen.
5. **Choose "Add Meta Pixel code to website yourself".** You will most likely have three options here. The other two hand the job to a developer or to a partner platform, and you do not need either of them.
6. **Click "Copy code".** This copies your Meta Pixel base code. Leave this window open, because you are coming back to it at the end.
7. **Open your site settings in [Webflow](https://webflow.com/).** Click the three dots on your project, then click "Settings". These steps assume you are using Webflow, and if you are on another website platform, everything here will be close enough that you can follow along and apply it to yours.
8. **Paste your pixel code into the Head code field.** Click "Custom code" in the left menu, paste the code into the "Head code" field, then click "Save". The easiest way is usually to do it in your sitewide settings rather than adding it page by page.
9. **Paste your pixel code into the head of every page on your site.** Open your site in the Webflow editor, click the page dropdown at the top, click the gear icon next to a page, scroll all the way down to "Custom code", paste the code into the "Inside <head> tag" field, then click "Save". Do this for every page you should already have built in the [Funnel Pages](https://www.skool.com/leadgenerationacademy/classroom/94f7e3ec?md=68a8c2b7f11e41b1996f9f6d67084446) course. There are situations where you would not want the pixel on every page, but those will be talked about later. For now, especially if you are already not successful with ads, just put it everywhere.
10. **Publish your website.** Click "Publish" in the top right and select your domain. You should already have your custom domain connected to this site. The pixel does nothing while the code is sitting in an unpublished draft.
11. **Go back to [Events Manager](https://eventsmanager.facebook.com/events_manager2) and click "Done".** Work through the three setup steps and finish them off. This is what tells Meta you are finished setting up the pixel.
12. **Confirm your pixel is receiving events.** Open your pixel in Events Manager and look under Events. There should be at least one event showing, and at minimum one PageView.
13. **Install the [Meta Ads Data Advisor](https://chromewebstore.google.com/detail/meta-ads-data-advisor/fdgfkebogiimcoedlicjlajpkdmockpc?hl=en) extension and check your live page.** Open your live website, click the extension, and you should see Meta Pixel listed as Active. If it comes back empty, the code did not make it onto the published version of the page.

### Completion Audit

- Did you open Events Manager?
- Did you click "Datasets"?
- Did you select the pixel you want to use?
- Did you click "Set up Meta Pixel"?
- Did you choose "Add Meta Pixel code to website yourself"?
- Did you click "Copy code"?
- Did you open your site settings in Webflow?
- Did you paste your pixel code into the Head code field?
- Did you paste your pixel code into the head of every page on your site?
- Did you publish your website?
- Did you go back to Events Manager and click "Done"?
- Did you confirm your pixel is receiving events?
- Did you install the Meta Ads Data Advisor extension and check your live page?

---

## Video Transcript

Automatic captions. Timestamps are minutes:seconds into the video.

[0:00] So the next step is going to be taking your pixel and basically putting it on your website. You can, this used to be called the Facebook Pixel Helper, apparently. And this is the first time I'm learning about it. It's called the Meta Ads Data Advisor. Oh my God. So realistically, so let's open it. Let's open up what we have here. I have a tab limiter here, so I'll open it up. Oh my gosh. Facebook has been. So anyways, basically what you're going to do is you're going to go to, you're going to go get your data in Facebook ads. You're going to get your pixel from there. So if you don't know how to do that, go to events manager.

[0:47] You'll click on data sets on the right hand side. You'll do it and you'll get a code that looks like this. You want to get the, you want to get the one where it says install manually. So I just copy and pasted this code. You want to go to whatever your website platform is. If you use a no code or an AI builder, just give it to this until it to put it specifically in the head. That's where you want it in the head, just like this. And then you also want to make sure you hit publish. Very important step to publishing the pixel properly. Eventually, even you could do this now if you want, but it's step five. You want to hire someone to do the Facebook conversions API, but the pixel is going to be good enough for this phase with your first 10 clients if you're inclined to do it.

[1:35] And then we'll go back what it can do is we're going to go to this thing here. And we'll download this and it will show up up here. So whereas it meant a dad's just not used to that, you know what I mean? Just not used to that name. So then we're going to go to our website and we're going to click this and see it says metapixel's active here, one event. So page view event is here. That's really all it should say for now at this step. So I have done it correctly, basically. So if you if you don't know if you've done it correctly, make sure you have that pixel advisor thing and then you'll see so in the head, however you do it on your platform.

[2:25] This is web flow and then install that and then make sure it's working.

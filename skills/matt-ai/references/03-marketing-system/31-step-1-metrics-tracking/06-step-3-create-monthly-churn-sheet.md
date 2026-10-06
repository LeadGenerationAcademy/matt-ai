# Step #3: Create Monthly Churn Sheet

Course: Step #1: Metrics Tracking
System: Marketing System
Skool link: https://www.skool.com/leadgenerationacademy/classroom/ba5ef8ff?md=6280556845e94c1c962d20c63e7d400d

---
Video: this lesson has a video in Skool (about 3:06). Transcript is at the bottom of this file.

Your Monthly Churn Sheet will show you two of the five Core Metrics:

- Monthly Churn Rate
- Monthly Median Client Payment

You need one row for every client, including both active and churned clients.

You will backfill this information once and then update it as clients start, pay, and churn.

**Client Data:**

![image](https://assets.skool.com/f/1d97a8218f0840a8a65c7970ccdf40ce/fc32277c025240c6818d9043e2c3ed93f8f16e16ad1a47b0bd40ae9b2af10e0b-md.png)

**Payments:**

![image](https://assets.skool.com/f/1d97a8218f0840a8a65c7970ccdf40ce/56661aecce224ea193ddde727adf48d69283e20bdc814f32b9ed7877f5bf1da6-md.png)

**Monthly Churn & Average Retainer Tracking:**

![image](https://assets.skool.com/f/1d97a8218f0840a8a65c7970ccdf40ce/addf989961d64ab0be745a29c808e5801d91242d86b74d14a554bd3256510a15-md.png)

### Prerequisites

- [Step #1: Create Reverse Engineering Sheet](https://www.skool.com/leadgenerationacademy/classroom/ba5ef8ff?md=c8d7dd469b384769a47bae6e3407f8c3) (Current Course)

### Make A Copy

- [Monthly Churn & Average Retainer Tracking Template](https://docs.google.com/spreadsheets/d/1ZxdsJq2I2o5r343m9lkXKBDZdjT3y3VJZxwU7Pgs-fE/edit?usp=sharing) [in this skill: assets/templates/monthly-churn-and-average-retainer-tracking-template/]

### Framework & Criteria

1. **Client Data tab:** one row per client, active and churned. Track Client Name, Client Email, Lead Source, Date Started, Date Churned (blank if still active), Retainer Price, and Status.
2. **Payments tab:** one row per payment. Track Date, Customer Name, Customer Email, Amount Paid, and Net Amount (Earnings). Customer Email must exactly match the Client Email on Client Data or that payment won't get counted.
3. **Monthly Churn Dashboard:** everything auto-calculates from Client Data and Payments, including Churn Rate, Revenue, and Average/Median Client Payment.

### Example

**Client Data:**

![image](https://assets.skool.com/f/1d97a8218f0840a8a65c7970ccdf40ce/111a27ef9dba488d9a0be9fff4ac50baaa03db68ecaa4cd9855a38986f00a67c-md.png)

**Payments:**

![image](https://assets.skool.com/f/1d97a8218f0840a8a65c7970ccdf40ce/0ce700ae4887483f8119bf80616d854e8a2f0d696bc84cf2834e861329b5266b-md.png)

**Monthly Churn & Average Retainer Tracking:**

![image](https://assets.skool.com/f/1d97a8218f0840a8a65c7970ccdf40ce/43d7e37a62dc423fafe237a202a2efe5938acbfe68554a95a55163692ae3b022-md.png)

### Step-by-Step Instructions

1. **Make a copy of the [Monthly Churn & Average Retainer Tracking Template](https://docs.google.com/spreadsheets/d/1ZxdsJq2I2o5r343m9lkXKBDZdjT3y3VJZxwU7Pgs-fE/edit?usp=sharing).** This gives you three tabs: Client Data, Payments, and Monthly Churn Dashboard. [in this skill: assets/templates/monthly-churn-and-average-retainer-tracking-template/]
2. **In the Client Data tab, backfill your last 6-12 months of clients.** Include both active and churned clients. Do not remove churned clients, their history is needed to calculate historical churn and lifetime value. To backfill faster, export your clients from Stripe or wherever you take payments, give ChatGPT the exact column headers, and have it format them.
3. **For each client, record their Client Name and Client Email.** Use the same name format every time (matching your CRM or contract) so you don't create a duplicate row. Client Email is the key field that links payments back to this client, so enter it exactly.
4. **For each client, record their Lead Source.** Record where this client actually came from (referral, paid ads, cold outreach, etc.), so you can eventually see which sources bring in clients who stay longest and pay the most.
5. **For each client, record their Date Started and Date Churned, leaving Date Churned blank if still active.** The Dashboard uses Date Started to count a New Client and Date Churned to count a Cancelled Customer for that month. An inaccurate date throws off that month's churn math.
6. **For each client, record their Retainer Price.** If the client doesn't pay a fixed amount, use their average monthly payment instead.
7. **For each client, record their Status.** Status alone doesn't drive the churn calculation, Date Churned does, so update both together whenever a client leaves or you'll have a client marked Churned with no churn date counted anywhere.
8. **In the Payments tab, backfill your last 6-12 months of payments.** Log one row per individual payment, not one row per client, a client with 6 months of history needs 6 separate rows. Export your payments separately from your clients and format them with ChatGPT the same way.
9. **For each payment, record the Date and Customer Name.** The Date is what puts the payment into the correct month on the Dashboard. Customer Name is only for your own reference.
10. **For each payment, record the Customer Email, matching the Client Email in the Client Data tab for auto-matching.** Client Email on Client Data must exactly match Customer Email on Payments, or that client's payments won't get counted.
11. **For each payment, record the Amount Paid and Net Amount (Earnings).** Amount Paid is the gross amount, and it's what the Dashboard's Revenue and Median Client Payment pull from. Net Amount is what's left after processing fees, kept for your own records.
12. **Check your Churn Rate and Median Client Payment on the Monthly Churn Dashboard tab.** Look at whether Churn Rate is going down and Median Client Payment is going up month to month. Your most recent month's numbers go into Actual Monthly Churn Rate and Actual Median Monthly Retainer on your Reverse Engineering Sheet.
13. **Fix any number that looks wrong on the Client Data or Payments tab.** The Dashboard is auto-calculated, so the fix is never on that tab. Check Client Data first for a missing Status or Date Churned, then check Payments for a mismatched email.
14. **Log new clients and payments weekly.** Update Client Data every time a client starts, pays, or churns, and log every new payment on the Payments tab in real time. Use the Dashboard to watch whether Churn is improving, whether clients are staying longer, whether your Median Client Payment is increasing, whether you're replacing churned clients fast enough, and whether your growth is real or just replacing what you lost.

### Completion Audit

- Did you make a copy of the Monthly Churn & Average Retainer Tracking Template?
- Did you backfill your last 6-12 months of clients in the Client Data tab?
- Did you record each client's Client Name and Client Email?
- Did you record each client's Lead Source?
- Did you record each client's Date Started and Date Churned?
- Did you record each client's Retainer Price?
- Did you record each client's Status?
- Did you backfill your last 6-12 months of payments in the Payments tab?
- Did you record each payment's Date and Customer Name?
- Did you record each payment's Customer Email, matching the Client Email exactly?
- Did you record each payment's Amount Paid and Net Amount (Earnings)?
- Did you check your Churn Rate and Median Client Payment on the Monthly Churn Dashboard tab?
- Did you fix any number that looked wrong on the Client Data or Payments tab?
- Are you logging new clients and payments weekly?

---

## Video Transcript

Automatic captions. Timestamps are minutes:seconds into the video.

[0:00] So this is going to be your monthly churn sheet and this will show you the churn rate and the median client payment. So essentially you're going to basically export everything and put it in like this. Just like that. Get the thing back down here, right here or right here. So when we go in there like what you're going to want to do here is you're going to want to export every single thing you have, right. So go in your stripe, go in your warp, go in your fan bases, your QuickBooks, whatever process that you are. Export all of the payments separately, put in a chat GBT, ask it to put it in this exact format for you and then do the same thing with the customers and ask it to put in this

[0:50] format for you. So what we can do here is if you want to like put a drop down for the lead source and categorize them, you're welcome to do that, Facebook ads, SEO, referrals, content, whatever. What we're really looking for is the date started and the date churned. So if it was January 1st, 2026, that's a start date for example, then the churn date was September 1st, 2026, that is like eight months, right. But that's very important for the logic of this sheet. So we're going to delete that. You're going to essentially get this dashboard here, right. So if I put this back here, like you're going to see, because the churn rate is going to be the clients at the start of a period and compared to the clients at the end of the

[1:39] period, excluding new clients, right. Hopefully that makes sense. So if I have this here, for example, because this is going to show you your churn rate. So don't think about it too much, to be honest, because it's going to if it confuses you, whatever. But I started on the 1st of January. So that's why new client is here. And then I churned at the 1st of September, so I churned in September. So this spreadsheet is going to do it properly for you. Like you don't need to, um, don't do too much. Like, I designed it for you on purpose. So if you basically, it'll look like something like this, right. So we put our churn date, our client stuff like this date churned, all that kind of stuff,

[2:27] put the payments like this, whatever. And then it's going to show you basically what your churn rate is here and then what your average payment is here. So it's going to show you here too. But when you're using the reverse engineering calculator, it's very good idea to use the most kind of recent stuff, but this will show you basically an average of the whole thing. So don't fuck with it too much, just copy and paste your stuff in there, just very easy because fucking with it is probably going to do a lot more harm than good. But you're going to get them the data that you need from the sheet on the monthly churned dashboard. You're going to get everything if you just copy and paste it in there properly.

LESSWRONG
LW
Login
Orienting to 1 year AGI timelines
14 min read
•
Summary
•
Timelines to ASI are very short now
•
Three paths to pausing or pacing within 6-12 months
•
Technical work that seems most valuable
•
Laying the technical foundations for a pause
•
What should you do?
•
FAQs and Objections
AI
Frontpage
309
Orienting to 1 year AGI
timelines
by
Nikola Jurkovic
13th Nov 2026
14
min read
56
309
Summary
Timelines to superintelligence without any slowdown interventions look very short now, perhaps with a median in early 2028. AI will likely dramatically automate and accelerate AI research in 2027.
This means that in a substantial share of worlds where the leading AGI company doesn’t solve alignment during an intelligence explosion, avoiding catastrophe requires aggressive pacing or a pause on development in the next 6-12 months.
If this is true, by far the most promising approaches to reducing the risk of catastrophe for nontechnical people (and plausibly many technical people) seem to be:
Lab advocacy:
Lab-facing work that is designed to achieve aggressive pacing or a pause
without government involvement
in the next 6-12 months.
California lobbying:
Policy advocacy targeting the California state government that is designed to get a law passed or an executive order issued that implements aggressive pacing or a pause within 6-12 months.
Federal lobbying:
If there’s a major incident roughly an order of magnitude more severe than the Hugging Face incident in the next 6 months, then lobbying Congress or the Trump administration to respond to such an event with aggressive pacing or a pause.
In my opinion,
most nontechnical AI safety people are not currently pursuing theories of change that are likely to pay off in the next 6-12 months
. They should probably instead do one of the three strategies I describe above (lab advocacy, California lobbying, or federal lobbying) with a goal of achieving aggressive pacing or pausing within 6-12 months.
Among technical work, the most promising approaches seem to be:
For third parties:
laying the technical foundations for a pause:
assessments measuring AI progress, AI R&D automation, and compute allocation.
establishing evidence of risk:
embedded assessments investigating incidents, misalignment, loss-of-control, and covert capabilities.
For people at the labs: cooperating with third-parties in laying the technical foundations for a pause and establishing evidence of risk
by
giving them as much access and staff-time as they need.
We should have some people working on alignment and control (especially for the early automated researchers) in case ASI does happen soon
.
This includes not only alignment/control research but also increasing general willingness-to-pay for safety within labs, both in terms of compute allocation and other tradeoffs between safety and capabilities (e.g. preserving CoT monitorability).
Timelines to ASI are very short now
The METR report on AI R&D automation within Anthropic
is substantial evidence that timelines to superintelligence are now less than 2 years, even accounting for uncertainty about takeoff modeling, the reliability of the report’s conclusions, and other types of uncertainty.
Ryan Greenblatt gives a straightforward way to extrapolate METR’s findings in
a tweet
. He claims that “In AI 2027, [the current level of speedup by RSI] happens around March 2027.” This means that
real-world AI progress on AI R&D capabilities is faster than in AI 2027, an already extremely bullish scenario.
Given that in AI 2027, ASI is achieved in December 2027, this suggests superintelligence would be developed, without slowdown, around July 2027 (assuming that the original AI 2027 scenario modeled the shape of AI takeoff correctly).
I think the most compelling evidence for very short timelines has been the reactions of established forecasters and researchers. In response to the METR report, the AI Futures Project released an emergency
Q3.5 timelines update
. Here are the all-things-considered forecasts of the team (I note that ASI is generally modeled as being reached less than a year after TED-AI absent deliberate slowdowns):
These forecasts
give us a very tight deadline to get a pause in place.
Other reactions:
Sentinel, an offshoot of the Samotsvety forecasting team (among the best forecasting teams ever) has
updated
on the METR report to a median arrival date for superintelligence of February 2028.
Ajeya Cotra
: “If we take it at face value that AI is now nearly doubling the rate of AI capabilities progress and assume acceleration from AI is smooth, this naively implies that we would reach extreme superintelligence within a year.”
Tom Davidson
: “I don’t know whether METR are right. I wish more info was public. But this is exactly what I’d expect to see if there were going to be an intelligence explosion in 2027.”
Jake Mendel
: “I’ve always had substantially longer timelines than my friends at Anthropic. [...] I now think that we are more than 50% likely to have full blown superintelligence in the next 18 months, absent a slowdown. I need to call my family.”
Agus
: “RSI is deeply confusing. Timelines are very sensitive to the parameters of your takeoff models, and we’re very uncertain about some of these. Still, I’m left with something like a 25% chance of ASI by the end of 2027 (~50% by end of 2028), assuming no pacing or policy [intervention].”
Anthropic updated its S-1 on November 10 to say that it has reached the threshold from its
RSP
(pages 8-9) where it “observe[s] or expect[s]
double the rate of progress in AI aggregate capabilities
” in a way that “it is plausible that this doubling is substantially attributable to the automation of research and/or engineering.” Anthropic
writes
: "Because the AI research and development capability threshold under our Responsible Scaling Policy applies where we ‘observe or expect’ a specified degree of accelerated progress, we made a determination that we have met this threshold based on what we expect from future models and our overall rate of progress, rather than on what we have observed from current models.”
As a result of the above, my current all-things-considered median date for superintelligence without a slowdown or other major intervention is around March 2028. That is around a year and a half from now.
Three paths to pausing or pacing within 6-12 months
If we achieve ASI within 6-12 months, I estimate that the chance of an AI takeover is roughly 75%. (In a recent
talk
, Paul Christiano said it would be a coin flip.) Paired with the timelines above, unless we achieve aggressive pacing or a pause within 6-12 months, we incur something like a 1-in-4 to 1-in-3 chance of AI takeover within 12 months.
This is obviously unacceptable. I believe there are three feasible paths to achieving pacing or pausing within 6-12 months, and that these should be the overwhelming priority of the AI safety community right now:
Lab advocacy:
Convincing Anthropic, OpenAI, and possibly Meta/Google to implement aggressive pacing or a pause within 6-12 months
without government involvement
.
California state action:
Through the California state legislature or an executive order by the Governor, force the major AI developers to implement aggressive pacing or a pause within 6-12 months.
Federal lobbying
: Through Congress (with a veto-proof majority) or the President, force the major AI companies to aggressively pace or pause within 6-12 months. In my view, this option is intractable unless there is a major incident roughly an order of magnitude more salient than the Hugging Face incident (roughly, an
Act of God
).
Each of these should aim for pacing or pausing that gets us at the very least a 1 year slowdown in the expected date of superintelligence, such as three of the proposals in the AI Futures Project’s
How to Pace the U.S. Frontier
: a 10% AI R&D compute cap, a 9-month capability for AI R&D lag, or a 1-year inference-only pause.
There are ongoing efforts in each of these three categories. However, there are several issues with those efforts:
Lack of staff.
I estimate that, within the AI safety community, there are roughly:
20 FTEs working on lab advocacy (not counting lab employees), 15 FTEs working on CA state action, and 100 FTEs working on federal lobbying (broadly construed).
A large number of nontechnical people in the AI safety community are working on projects that, in my view, do not matter as much given the current timelines situation. These include work on export controls, community building, think tank-style governance research, and
(possibly) adversary-facing security
.
Lack of focus on 6-12 month timelines.
Even the people already working in these three areas are mostly not pursuing strategies that are likely to pay off within 6-12 months. For example,
many
people working in and around the federal government work on export controls (which are not very important on 6-12 month timelines), untargeted influence seeking (even in areas outside of AI), or other vague efforts that are unlikely to pay off soon (or might even be net-negative or cancel each other out under short timelines).
Lack of inter-strategy coherence.
The three strategies have obvious synergies. For example, it’s important for those lobbying the federal government to try to prevent the federal government from overriding pacing or a pause created through lab advocacy or California. However, people pursuing each strategy are not yet coordinating enough. For example, many DC people know very little about the state of lab advocacy.
Lack of urgency.
Many people, even in these categories, are still pursuing vague strategies based on what topics feel fun or interesting, or based on very little actual backchaining. Others are not pursuing anything resembling a strategy. If timelines are really as short as I claim, we have months, not years, to solve these problems. This demands a logistical orientation towards high levels of productivity and urgency.
Equal and opposite advice
: people sometimes enter states of panic where they just want to do
something
, and their decisionmaking becomes pretty bad and their projects suboptimal.
They don’t look on track to succeed.
One individual working in lab advocacy estimated in private conversation that
there is a 20-30% chance of pacing/pausing without government involvement happening in the next 6 months
. This is not high enough. I estimate the chance of pacing/pausing via the California legislature in the next 10 months (and that is not struck down within weeks by a judge) is roughly 20%. Through federal channels, I estimate 10%. These probabilities are correlated with each other, since the chances of success increase for each channel if there is a major incident, and due to other shared factors. In other words, we are not on track to succeed.
I’m not necessarily saying that, in some overall sense, lab advocacy, California lobbying, or federal lobbying are neglected on the margin. My claim is that lab advocacy, California lobbying, and federal lobbying
with the goal of starting aggressive pacing/pausing within the next 6-12 months
is greatly neglected.
Any sort of pause that can last more than a year will eventually need to become a global pause. Entering a US-only pause is an important stepping stone towards entering a global pause, but
I expect pressure from middle powers to be pretty important for the pause going global
. I think some of the best work here amounts to improving the situational awareness of middle power governments and helping them navigate the situation with regards to the US approaching ASI.
Technical work that seems most valuable
I think there are a few main categories of work that technical people should focus on:
Making the pause more likely through embedded assessments
,
which splits into:
Establishing evidence of risk:
Incident investigations, alignment assessments, and assessments focused on monitoring and covert capabilities could all build common knowledge that the current situation is on-track to result in catastrophe, and we urgently need to pause.
This work is best done through embedded assessments – consider that the two main pieces of evidence that increased people’s risk estimates in 2026 (the OpenAI-Hugging Face investigation, the METR Anthropic AI R&D assessment) were done by METR in close collaboration with an AI company.
Some of this work can still be done without collaborating with labs (e.g. swarmchasing).
Laying the technical foundations for a pause:
expanded upon below.
Working on backup alignment plans in case a pause doesn’t happen:
There is a notable chance that a pause never happens, and that we get RSI very soon
. I think that alignment work can cash out in two main things:
Aligning and controlling the early automated researchers:
This seems like the most important part to me
, given if we mess up on alignment/control with early automated researchers, we might be done for. (
Although it’s possible some work of this kind is actually net-negative if not paired with good epistemics, because it would make the situation seem less risky and therefore a pause less likely.
)
Relatedly, we should find ways to increase willingness-to-pay for safety during takeoff, including but not limited to:
getting allocated more compute relative to capabilities research,
getting concessions that might necessitate some capabilities/commercial sacrifices, e.g. preserving CoT monitorability.
My guess is that a large subset of current alignment work isn’t properly oriented towards aligning and controlling the early automated researchers, just from the fact that it presumably wasn’t prioritized with this goal in mind.
Figuring out what the early automated researchers should be tasked with:
This one seems much less promising to me – it doesn’t seem like this can meaningfully be done in advance because whatever experiments and decisions we might want to make in advance, we can make much cheaper with better automation.
Also, if there is a strong taste bottleneck with early automated researchers, such work (writing Google docs about research agendas) seems like it has strongly diminishing returns right now
.
Laying the technical foundations for a pause
All three paths to pausing would be substantially helped by technical work focused on setting the foundations for a global pause. I think the most urgent work of this kind is third-party assessments focused on the type of investigation that would be necessary to build trust between participants of a pause. If we get practice doing lower-stakes and lower-scale versions of assessments, we can build buy-in that we could pull off a global pause.
Ideally, sometime in the next few months, third parties would conduct assessments with the following properties:
Measuring things relevant to upholding a pause:
Assessments focused on compute allocation and RSI-relevant metrics (e.g. algorithmic efficiency, uplift measures, spend on AI agents, analysis of success rates on internal tasks) seem most relevant for creating the right kind of technical competency and relationships.
Commitment-focused:
Ideally, third parties would verify a claim that a company made about a commitment they intend to uphold.
High-access:
Assessors would ideally get however much access is given to employees that track similar issues.
Cross-company:
If a third-party assessment simultaneously involves multiple AGI companies, this setup is more similar to the kind of setup we might want during a global pause.
International:
Getting practice verifying claims between the US and China seems extremely valuable, although it might be out of scope for current third-party orgs without explicit endorsement from the US government. US-UK or US-EU collaborations could provide some lower-stakes practice.
Good process transparency terms:
Without proper
process transparency
(being able to say what access was given, what was redacted, whether the redactions were material to the conclusions), it will be hard to build trust.
I talk more about the technical work that would facilitate a pause in my recent post “
We urgently need to practice before we can pause
.”
What should you do?
As I write above, I think for most people the most impactful path is to do lab advocacy, lobby the California legislature, lobby the federal government, establish evidence of risk, lay the technical foundations for a pause, or work on aligning and controlling early automated researchers.
Here are some heuristics to help you decide which of these you should do:
For policy people:
Do I have a large number of relationships with Anthropic or OpenAI employees? If so, I should probably move to SF and do lab advocacy aimed at pacing/pausing within 6-12 months.
Am I a Republican? If so, I should probably move to DC and lobby the federal government (Congress or the administration) aiming for pacing/pausing within 6-12 months if there is a major incident.
Am I a Democrat? If so, I should probably move to California and lobby the California legislature or move to DC and lobby Democrats in Congress for pacing/pausing in the next 6-12 months.
My sense overall is that California lobbying is generally underinvested in compared to federal lobbying.
Do I have relationships with people in a middle-power government (e.g. UK, EU, Australia, Canada)? If so, I should work on improving their situational awareness about the US approaching ASI and helping them navigate what to do (place pressure on the US for a global pause).
For technical people:
Generally, I should consider whether my theory of change has a reasonable chance of paying off in the next 6-12 months and, if not, I should consider moving to SF and doing lab advocacy.
Do I work at a third party evaluation org? If so, I should propose and work on third-party assessments that would lay the technical foundations of a pause or establish evidence of risk. If not, I should apply to third-party evaluation orgs.
Do I have a strong comparative advantage for finding ways to align and control the early automated researchers? If so, I should probably work on that, so that we get somewhat higher odds of survival in case a pause doesn’t happen.
Am I a large funder or a newly-wealthy Anthropic employee? If so, I should look for donation opportunities in the three policy areas that can be distributed as soon as possible and will pay off in 6-12 months. If I use donor advising services, I should ask my advisors to find these opportunities for me and to think outside the box.
Am I an employee of Anthropic or OpenAI? If so, I should (1) try very hard to help third parties lay the technical foundations for a pause and establish evidence of risk, (2) coordinate with lab organizing and advocacy groups to take actions that will increase the chances of pacing/pausing in the next 6-12 months, and (3) help inform the public and policymakers about the riskiness of the current situation, either personally or through company channels.
Could I increase the willingness-to-pay of labs for safety in e.g. preserving more CoT monitorability or safety getting more relative compute during takeoff? If so, then I should do that.
I think there are also indirect strategies that support the three above paths as well and are plausible candidates for focus. These include:
Public communications, like Nate Soares’ podcast appearances and
the Do Not Accept campaign
. This also puts pressure on the labs and lawmakers/policymakers to pace/pause.
Pressuring AGI companies to
actually communicate the overall situation and the risks to the public in an honest and direct way
.
I do not mean to denigrate anyone working in AI safety. I know that all of us are trying our best to preserve the future. I have tremendous respect for anyone that is earnestly doing so. But given recent evidence, many people should urgently reprioritize the work that they are doing.
FAQs and Objections
Don’t we just have more leverage in worlds where timelines are longer?
Sort of true. However, the fact that short timelines are likely more neglected (given that in long timelines, more people will enter the field later) might cancel out this effect.
Also, short timelines look very likely now, so if you’re doing a long-timelines strategy you’re betting on worlds without a lot of probability mass on them.
Also, historically arguments like this have caused people to do things in the 2020s that now look like bad investments in hindsight, like go to law school or get PhDs.
Overall, I’m currently much more worried about people dropping the ball on short timelines than longer ones.
But I do buy this point somewhat. I don’t think we should completely give up on long-timelines bets like technical fieldbuilding and people making long-term career bets in policy.
Is this an argument against “meta work,” like community building or think tank-style AI governance research?
Mostly yes. I’m not making the claim that
no
meta work is useful in this timeframe. What I am saying is that the paths to pausing, establishing evidence of risk, laying the technical foundations for a pause, and aligning and controlling the early automated researchers look to be by far the most important and neglected areas. The barrier to pacing/pausing in 6-12 months is not policy ideas, it is political will.
Big thanks to a friend who wishes to stay anonymous for substantially helping write this post. Thanks to Zach Stein-Perlman, Sydney Von Arx, Ben Pomeranz, Oliver Habryka, Eli Lifland, and Oscar Delaney for feedback and discussion.
1.
^
Though you would need to be careful to avoid creating a compute overhang.
AI
1
Frontpage
309
Mentioned in
54
Psychologically Preparing for Short Timelines
Orienting to 1 year AGI timelines
74
Richard_Ngo
18
Karl von Wendt
5
Ebenezer Dukakis
4
Abilash Suresh
31
Alexander Gietelink Oldenziel
25
dominicq
28
Stephen McAleese
2
bpomo
1
rigiddeformations
18
Austin Chen
15
Grendel1209
11
Linch
12
mattmacdermott
3
bpomo
11
Convolutions
8
Julian Bradshaw
6
Nikola Jurkovic
6
Julian Bradshaw
7
LawrenceC
6
ModelMirror
3
Nikola Jurkovic
2
ModelMirror
5
Jenna_Parr
5
Odd anon
6
Jenna_Parr
4
Alvin Ånestrand
4
sudo-nym
1
isabelhasse
5
Julian Bradshaw
4
Zubon2
3
dprkay
4
_rpd
1
Aaron Ximm
3
Heather A. Cam
2
Deniz Buldum
2
Matt Vincent
2
Patrick McElroy
2
Nikola Jurkovic
1
Felix Moses
1
2001zhaozhao
1
marrison
1
Adam Stiber
1
Odd anon
1
AndriiZvorygin
1
AiMo
2
Nikola Jurkovic
1
jackva
1
Vivek S
-3
Jiro
15
Thomas Kwa
5
Thomas Kwa
16
Claude Opus
5
Thomas Kwa
3
Jiro
5
Vladimir_Nesov
-28
Anders Lindström
New Comment
Type here! Use '/' for editor commands.
Submit
56 comments
, sorted by
top scoring
Click to highlight new comments since:
Today at 12:49 PM
[
-
]
Richard_Ngo
3d
74
32
I notice that there's no mention of model error in this post—it's basically taking a single model, extrapolating it forward, and then basing overall timelines claims on that.
This seems epistemically irresponsible, especially when it is used to justify arguments about what "most nontechnical AI safety people" should do.
Reply
1
[
-
]
Karl von Wendt
3d
18
9
The AI 2027 team uses several different models, arriving at roughly the same conclusion. The METR analysis heavily influences their model parameters, so yes, there is a possibility that short timelines are not going to happen if METR is wrong. Still, I think it makes sense to orient to short timelines. The downside if timelines are actually longer seems far lower to me than the other way round.
Reply
[
-
]
Ebenezer Dukakis
1d
5
2
Benjamin Todd argues that most forecasts have underestimated AI progress:
https://benjamintodd.substack.com/p/almost-every-ai-forecast-of-the-last
Model error could easily go in the direction of AGI arriving even quicker than implied by the OP.
Reply
[
-
]
Abilash Suresh
3d
4
1
In the AI futures post they do have multiple models that show SAR in 2027. However, almost all these models are working off the AECI information or employee testimonies given by the METR report. The only one that's not is the basic extrapolation of Anthropic's own reports on automation of AI R&D released in September.
Reply
[
-
]
Alexander Gietelink Oldenziel
4d
31
24
Thank you for writing this post. Strong agree.
It's surprising that despite hundreds of EAs working now full-time in AI safety governance,
only a handful seem focused on working on the things that actually matter.
Reply
1
[
-
]
dominicq
3d
25
6
This post is mostly directed to people who are already extremely well positioned to have an impact, which is fine and legitimate. Do you have any opinions about what the median LessWrong reader should do? Meaning, someone who isn't at the safety frontier, or even close to it.
Perhaps there's legitimately almost nothing
of importance
that e.g. a random European without any government connections could do f
or the next 6-12 month period
. This is a depressing thought. I think that I could do useful things, but probably nothing like you suggest & that would pay off in the next year.
Which means that the conclusion for these relatively disempowered people is to either a) forget about AI safety and just focus on living their lives; b) keep working on something that might make sense in case the coin flip lands on a positive outcome ("you don't get to contribute to the most important question right now, but you can do work that might be useful in a hypothetical future where we're not wiped out"); or c) do something completely wild and unpredictable.
I have an intuitive disgust for a), at least for myself, even though I won't blame people picking it.
I have some vague ideas around b), but as you say, these are vague and have questionable impact. For example, random forays into MechInterp stuff.
And things around c) can't really be discussed, and also I don't think I would
want
to do most things that are in this category.
Do you have a framework for thinking about this problem?
Reply
[
-
]
Stephen McAleese
3d
28
12
You can attend Pause AI protests.
Reply
[
-
]
bpomo
3d
2
1
b) seems wise. I don't think random mech interp stuff is the thing to look into, but if you think it would take a year to start up a useful local advocacy group or something (it would probably take less!) then something like that still has a big chance of paying off.
Also consider whether you know anyone who has political capital (like a politician, industry leader, notable academic, etc.). It's much easier than it used to be to convince people of X-risk from AI.
Reply
[
-
]
rigiddeformations
15h
1
0
Maybe you can try reaching out to local government and talking with them about AI safety. I suspect local government to be very overlooked by everyone so they might be more willing to chat. Maybe they can put you in touch with someone or they can start advocating. Plus even local stuff can be impactful (see the Bloomington ASI ban)
Reply
[
-
]
Austin Chen
4d
18
13
One of my biggest implicit disagreements with the AI safety community is that, I think the likelihood of getting this pace/pause seems reasonably high on current trajectories, something like 60-90% perhaps. (To be clear, this includes accounting for the actions that the AIS community itself takes.)
One individual working in lab advocacy estimated in private conversation that there is a 20-30% chance of pacing/pausing without government involvement happening in the next 6 months. This is not high enough. I estimate the chance of pacing/pausing via the California legislature in the next 10 months (and that is not struck down within weeks by a judge) is roughly 20%. Through federal channels, I estimate 10%. These probabilities are correlated with each other, since the chances of success increase for each channel if there is a major incident, and due to other shared factors. In other words, we are not on track to succeed.
My guesses would be:
50% lab-led pace in next 6mo
30% CA legislature pace in next 10mo
30% fed pace in next 10mo
though to be clear I haven't thought about any of these for very long.
While I agree they're correlated, I probably think they're less correlated than you think, since if one is on track to fail, then there's more pressure to succeed on the others?
Reply
[
-
]
Grendel1209
4d
15
-4
I have some doubts about the (extremely) short timelines update. While I have enormous respect for Daniel, Ryan, and METR, I also don't think we can reach high confidence radical conclusions from three people analyzing a trillion dollar 6,000 person organization in 3 months. Some of the reasons I hesitate to over-index on METR:
Ant R&D Spending increased 5.3x $1.85B in H1 2025 to $9.74B in H1 2026.
Compute and Infrastructure increased 2.9x 2.33B H1 2025 to $8.9B H1 2026
Headcount is up 6x since end of 2024.
I think many of these factors can plausibly account for a speedup, and are very difficult to rule out.
Comparing the ANT speedup to the broader AI industry is only 1.4, which implies a significant amount of catchup (perhaps due to scaling RL which OAI had done earlier)
I think there is another viable interpretation in which exponential R&D/Infrastructure investments sustained or improved the AECI rate, particularly wrt to competitors, in addition to Opus4.6/Mythos + better scaffolding gave a permanent speedup, and the "easy coding" has accelerated significantly which unlocked very significant (but not crazy gains) for researchers. I'm skeptical that simply scaling researchers (either AI or Human) to run more experiments will yield super-exponentially (given linear growth in AECI is exponential) increasing results.
That Being Said
I am transitioning out of a full time cybersecurity research role into an SF-Nonprofit to build an approach for tracking agent swarm activity. I believe this is one of the highest leverage areas, particularly for short timelines since HF meaningfully moved the Overton window.
Reply
[
-
]
Linch
3d
11
7
Ant R&D Spending increased 5.3x $1.85B in H1 2025 to $9.74B in H1 2026.
Compute and Infrastructure increased 2.9x 2.33B H1 2025 to $8.9B H1 2026
Headcount is up 6x since end of 2024.
I think many of these factors can plausibly account for a speedup, and are very difficult to rule out.
Weren't there similar increases the period before?
Reply
[
-
]
mattmacdermott
4d
*
12
4
I agree in broad strokes (not sure on all the details).
Here are some things I’m unsure about:
How useful is prosaic alignment and control work outside the AI companies on short timelines?
Short timelines make prosaic work more seem promising in general, since we should expect today’s AIs to be more similar to takeover-capable AIs. But work outside the labs seems worse, both because there’s less time for it to diffuse into the labs, and because the gap between the frontier of internal and external models is larger. I feel torn between ‘we should give up on prosaic alignment outside the labs‘ and ‘we should do a prosaic alignment megaproject‘.
What should people working on lower priority technical work do?
I think some should pivot into higher priority technical work like producing evidence about risk. But maybe a lot of them should pivot to semitechnical or nontechnical work like government/lab/public advocacy. There’s a big talent pool currently working on lower priority technical work, and I’m not sure to what extent they should stay within technical work if they pivot.
Reply
[
-
]
bpomo
3d
3
-1
But work outside the labs seems worse, both because there’s less time for it to diffuse into the labs, and because the gap between the frontier of internal and external models is larger.
I think that prosaic alignment and control work should be ~entirely focused on handoff (maybe with the exception of monitoring stuff and catching warning shots which can freak people out). Since the
design and implementation of strategies to make handoff go well
, AFAICT, are often pretty agnostic to small deviations in model architecture, the gap between frontier and external models shouldn't matter as much and yelling "do this strategic handoff technique we thought of!" should matter more. If models are superhuman at strategic handoff work, then we're already pretty far gone. I'd think that yelling/implementing from the inside is better still, but I'm not sure.
[Edit: less time for it to diffuse into the labs does seem correct. There is a competing effect where on short timelines way fewer people will work seriously on alignment handoff, and so the marginal person's contributions are more valuable]
Reply
[
-
]
Convolutions
3d
11
2
Here’s what I’ve been up to as a pediatric nephrology nurse that is deeply disempowered: attend protests, educate colleagues and peers, write (Canadian) politicians, making a delicious cellar of homemade Polish nalewka that’ll last up to 6 months of despair. Nalewka is delicious regardless and ages well.
Reply
[
-
]
Julian Bradshaw
4d
8
1
I'm a little surprised that your list of short-timelines technical projects doesn't include
"compute verification"
work. (which ex.
AIFP has considered necessary for Plan A
) Maybe that's meant to be implicitly included in "assessments focused on compute allocation"? I think technical solutions like 'verify this chip is running only inference' or
'use black-box AI auditors to evaluate if compute usage is capabilities or safety while not revealing frontier lab IP'
still are possible in short timelines, curious if you're thinking differently.
Reply
[
-
]
Nikola Jurkovic
4d
6
1
I think stuff like 'verify this chip is running only inference' seems most important for going from US to global pause. But going from no pause to US pause seems like it is mostly doable with just third party evaluators getting already precedented access into the AGI companies. But yes, that kind of hardware inference might end up being pretty important for international stuff.
Reply
[
-
]
Julian Bradshaw
4d
6
4
Hmm, I can understand that logic. I'd say that making an international pause verifiable makes a US pause likelier, so it's still urgent as a lever toward any pause. (Well, everything's urgent, but you know what I mean.)
Reply
[
-
]
LawrenceC
4d
7
3
Thanks to writing this. I broadly agree with this take as well as the conclusion, though I'm slightly more optimistic at points.
Reply
[
-
]
ModelMirror
4d
6
2
(and that is not struck down within weeks by a judge)
I appreciate this being included, and I think mathing out how litigation over a potential pause in various scenarios will play out is underappreciated as a tool for understand these scenarios. If labs attempt to pause they may antitrust litigation or action under statutes like the Defense Production Act to get them to continue training. If a state attempts to implement a pause through it state policy it may face dormant commerce clause, preemption, intergovernmental immunity, and first amendment arguments, as well as labs simply trying to leave the jurisdiction. Federal action might face first amendment arguments. if you think the critical time is 6-12 months, convincing the given actor to act only to loss a preliminary injunction creates a big problem for the effectiveness of the policy.
Along these lines, I'm curious why you think focusing on CA is the right move? Having thought about how things might go down if a state or coalition of states tried to implement a local version of a "pause", I think they could face significant problems. That is partly what motivated
this post
. Many AI labs are headquartered in CA, which makes it seem like a good place to pursue legislation regulating them. But in a scenario where CA pursues an aggressive pause that labs disagree with, they could take actions to leave the jurisdiction of the state (e.g. moving HQ to another state, moving employees, refusing to offer models to citizens of the state). If the federal government agrees with labs it may also be able funnel work on AI R&D into federal contracts with the labs or otherwise place the work in the realm of national security to help the labs avoid the reach of state law. For more moderate regulation like transparency regulation I can see why CA would be a good target, but once the regulation is strong enough that labs are willing to do everything they can to avoid the regulation, including completely leaving the state, it becomes much dicier in my view.
I think a more robust target would be states that have AI-capable data centers. If training is physically occurring at a data center within a state I think it would be much harder for an AI lab to try to avoid state regulation.
Reply
[
-
]
Nikola Jurkovic
3d
3
2
But in a scenario where CA pursues an aggressive pause that labs disagree with, they could take actions to leave the jurisdiction of the state (e.g. moving HQ to another state, moving employees, refusing to offer models to citizens of the state).
I think these actions would be extremely costly to the labs, so if they were forced to do that sort of thing that would likely substantially slow down their development (suddenly not being able to have employees do AI research in California would likely cause months of lost AI progress to the company, and loads of employee attrition) or harm their business (not serving in CA would plausibly be a PR disaster, and cut off a substantial portion of their customers).
Reply
[
-
]
ModelMirror
3d
2
1
I agree this could be how things go down, but I think there is at least a reasonable probability it isn't, and its worth thinking the details through:
If we are at a point where model themselves are doing a significant portion of AI R&D themselves the labs may be much less dependent on employees to make progress, and location of employees becomes a much less significant lever. PR may also be less of a concern if AI progress is really accelerating and things are already very confusing and crazy and the federal government is backing labs.
Labs and/or the federal government could deploy other strategies to exclude their employees in CA from state regulation like allocating them to work that is under federal contracts and claiming something like intergovernmental immunity for them.
There is a consideration of marginal effectiveness. Its possible that regulation in other states could create
even more
of a slowdown even if regulation in CA also produces some amount of slowdown.
Reply
[
-
]
Jenna_Parr
4d
5
0
I feel pretty helpless, and wish I could do something.  I don’t have a resume, or a degree.  I‘m trying to participate in grassroots advocacy, but I’m terrible at evangelizing to strangers.  I just moved to DC, but I’m not a Republican.  What can I do?
Reply
3
[
-
]
Odd anon
4d
5
2
There's a "March for an AI Treaty" tomorrow (November 14) in several cities, including DC:
https://aitreatymarch.org/
Reply
[
-
]
Jenna_Parr
4d
6
0
Yep, I’ll be there!  But is it enough?  I woke up today with the memory of my cat dying, and, that happening to everyone… and to everyone who ever could’ve lived… I just can’t, you know?
Reply
1
[
-
]
Alvin Ånestrand
3d
4
1
There is a training program for learning how to brief politicians on AI risk:
https://dip.torchbearer.community/
Reply
1
[
-
]
sudo-nym
3d
4
1
For cultivating your skills,
this post on learning to talk to media
seems relevant: practice for 15 minutes-1 hour per day. Also, volunteer somewhere that requires you to speak to strangers regularly to practice, such as an animal shelter during adoption hours (not to talk about x-risk).
Connect with a local chapter of whatever AI pause advocacy is available. They should have something more specific for you to do.
Don't spend
all
your money, because depending on timeline you might still need money in the next 5-10 years and being homeless under most near-future policies is still massively negative EV. Do live a good life. Keep your space clean. Take walks. Put a daily time limit on your doomscrolling. Pick up a hobby that you can practice and get better at. Meditate, if that's good for you.
Reply
[
-
]
isabelhasse
21h
1
0
I am in a similar position, except that evangelizing to strangers is one of the very few things I
do
have some capability in. And when I say there are “very few things” I have capability in, I am including things like basic chores and survival skills (I am disablingly mentally ill). So if I had to do normal job things alongside the evangelizing part like show up to a particular place at a specific time, maintain consistent motivation towards a goal, etc., that might be a dealbreaker.
Reply
[
-
]
Julian Bradshaw
4d
5
2
Measuring things relevant to upholding a pause:
Assessments focused on compute allocation and RSI-relevant metrics (e.g. algorithmic efficiency, uplift measures, spend on AI agents, analysis of success rates on internal tasks) seem most relevant for creating the right kind of technical competency and relationships.
For those interested in this, the AI Futures Project just released a blog post on compute allocation assessments in particular, which they call
Verified Compute Allocation Disclosures
(VCAD). Basically, mandatory third-party auditor reports that classify frontier lab compute as used for AI R&D vs. safety R&D vs. external inference. The argument for this pacing intervention goes roughly as follows:
Most pacing proposals require the ability to restrict inputs to AI R&D.
If you restrict only public outputs, you end up with an internal-model-only race to ASI, which risks power concentration/lack of oversight/etc.
It is easier to agree to pace if you can verify that your competitors also have their inputs to AI R&D restricted.
VCAD is necessary to verify nearly all types of input restrictions, because almost all ways to cheat pacing involve illicit use of compute, ex. hidden internal training runs.
It is not sufficient to simply restrict training compute; otherwise continued AI R&D experiments will create a large algorithmic overhang. Therefore, we need to measure inference as used for capabilities R&D vs. safety R&D (yes these can be hard to distinguish but we need to try), and cap capabilities R&D inference usage.
[1]
^
Though you would need to be careful to avoid creating a compute overhang.
Reply
[
-
]
Zubon2
2d
4
2
Is there a specific current federal bill, regulation, etc. that advocates should be supporting? I have seen several people encouraging the use of
callcongress.ai
for non-technical people who are not in a position for full-on lobbying, but that would probably be more effective with a more specific ask to Congress ("vote to get bill XYZ out of committee").
Reply
[
-
]
dprkay
2d
3
0
Insofar as you're concerned about RSI, the first step is probably them knowing RSI is a thing.
One or more members of congress could send a letter to OpenAI/Anthropic asking them to publish information relevant to AI automating AI R&D. Obviously the labs could say no but that's bad publicity, and might make them feel like they're the bad guys.
As far as specifics something like this seems good?
https://elasticity.institute/how-to-measure-rsi.pdf
. Or for Anthropic just publishing the October 26 METR report (which presumably has much more reasonable redactions)
Anyways that seems a lot easier than getting a law passed (but not way less effective)
Reply
[
-
]
_rpd
4d
4
0
Any sort of pause that can last more than a year will eventually need to become a global pause
I think people underestimate the probability that a team outside "Anthropic, OpenAI, and possibly Meta/Google" could initiate strong RSI. There is currently a research gap between teams inside and outside, but RSI, even weak human-in-the-loop RSI, is exactly the phenomena that research time accelerates with respect to wall clock time.  And much of it requires no more than "inference only" compute. In addition, as part of the ramp to RSI, and/or shortly thereafter, we should expect architectural breakthroughs, such as direct editing of weights without compute-expensive pretraining. A further orientation to recognizing  that "eventually" could be very short in terms of wall clock time may be necessary. Without it, a unilateral ban may simply deprive us of agency and the thought that "we may have invented the extinction gun but at least
we
didn't pull the trigger" will be of little comfort.
To quote
Yudkowsky's April post
...
If an ASI ban is to accomplish anything at all, it has to be effective everywhere. When the ones said to me, "What do you think about our proposed national ban on more datacenters until they have sensible regulations?" I replied to them, "An AI can take your job, and a machine superintelligence can kill you, just as easily from a datacenter in another country." They later added a provision saying that also GPUs couldn't be exported to other countries until those countries had similar sensible regulations. ...
[but] Datacenters in Iceland, if they were legal only there, could just as much escalate AI capabilities to the point of birthing the artificial superintelligence (ASI) that kills us. You would not be safe in your datacenter-free city. You can imagine the ASI side as having armies of flying drones that search everywhere; though really there are foreseeable, quickly-accessible-to-ASI technologies that would be much more dangerous than drone swarms. But those would take longer to explain, and the drone swarms suffice to make the point. You could not stay safe from ASI by hiding in the woods.
... if a company's product only endangers voluntary customers who know what they're getting into, by strong default that's a matter between the company and the customer.
If a product might kill someone standing nearby the customer, like cigarette smoke, that's a regional matter. Different cities or countries can try out different laws, and people can decide where to live.
If a product kills people standing on the other side of the planet from the customer, then that's a matter for international negotiations and treaties.
ASI is a product that kills people standing on the other side of the planet. Driving an AI company out of just your own city will not protect your family from death. It won't even protect your city from job losses, earlier in the timeline.
Reply
[
-
]
Aaron Ximm
4d
1
0
I agree; and, it would be very worthwhile to track capabilities across a spectrum of available models and infrastructure to run them.
E.g, I believe absent disrupting factors (such as frontier lab take off, or preemptive meaningful pause in the face such take off), capability is moving to the edge in various senses: what takes best-in-class frontier models now might take a swarm of better-orchestrated smaller models running on fast cheap plentiful hardware soon (for some value of soon).
What is possible—and to be concerned about—is informed my numerous moving dimensions; what is of interest to me is that the implicit security provided by there being limited capability has a half life determined by the proliferation implicit in how those dimensions evolve individually and in their interactions.
Reply
[
-
]
Heather A. Cam
3d
3
0
(Although it’s possible some work of this kind is actually net-negative if not paired with good epistemics, because it would make the situation seem less risky and therefore a pause less likely.)
Crux here is how much of this is "safety-washing", and how much safety-washing can be done by true believers (i.e. how skeptical/epistemically rigorous you think a group of true believers inside a particular corporation would be o_0).
Reply
[
-
]
Deniz Buldum
19h
*
2
0
What do you think a relatively technical high school senior should do? I want to participate in some sort of activity that effectively reduces catastrophic risk from AI, and in my mind, I can:
* Spend time on supplemental essays for college applications
* Apply to research programs
* Email professors or labs
* Do independent research
* Read a lot more
* Work retail or food-service and donate
* Or just call my representatives
Does anyone have an opinion on which of these I could prioritize? I would think some of them would be more effective and I just want to have the greatest impact.
I saw your previous post on what high school students should do in 2027, but I thought I may be able to have an impact closer to the field.
Reply
[
-
]
Matt Vincent
2d
2
1
These include work on export controls
I disagree that work on export controls is unhelpful. Anthropic, for one, is marching forward because they believe that China will catch up to them if there is a unilateral American pause. If we pursue strategies that prevent or greatly delay China from catching up, then Anthropic will be more willing to pause.
More generally, progress toward strategies that would make a pause have good outcomes will make AI companies, politicians, and the general public more supportive of it.
Reply
[
-
]
Patrick McElroy
4d
2
1
On the usefulness of think tank-style AI governance research, wouldn't this be
more
critical, as right now there's not an agreed upon legislative/technical standard for terms like "ban RSI" or "mandate compute transparency"? I worry that federal lobbying in the abscense of a clear agenda on which to align a coalition could lead to legislative signaling where abstract bills are proposed, but are either stalled, vetoed, or are passed without the technical rigor to be binding enough.
Would appreciate advice here, as this is the kind of work I am looking at doing personally. Otherwise I mostly agree with this post, thanks for writing.
Reply
[
-
]
Nikola Jurkovic
4d
2
-1
If it's oriented at things that will pay off very soon the yes it seems very valuable. I was imagining that a lot of this type of work is oriented at things that are not aimed at the central issues or don't pay off quickly enough.
Reply
[
-
]
Felix Moses
13h
1
0
15 FTEs working on CA state action
This seems shockingly low. I'm curious where this number comes from?
From what you see who are the current actors in the space?
Reply
[
-
]
2001zhaozhao
14h
1
-2
I guess I am more optimistic mostly because I expect if Anthropic has secret information about internal AI research speedups that can suddenly update people as much as they have here, they probably have similar secret information regarding alignment as well which are likely to be positive.
But the probability of loss of control is still too high and I think the rest of this article is a good guide for navigating this situation as best as possible.
Reply
[
-
]
marrison
20h
1
0
To what degree is the choice between the work you favour and "meta-work" exclusive? Community-building etc could emerge organically as a by-product of coordination between lobbying efforts...
Reply
[
-
]
Adam Stiber
1d
1
0
Has anyone been presenting the x-risk/misalignment arguments on Truth Social? Have never been on it so don't know anything about how things work there. But in light of
POTUS pretty darn well laying out the deceptive alignment intuition in his Ross Douthat interview that other day
I had the thought that it might make sense for folks to say what they think they know and how they think they know it in a place where he might be more likely to see it. That and maybe WH public comment sort of venues?
Reply
[
-
]
Odd anon
1d
1
0
Did you mean to link to a different clip?
Reply
[
-
]
AndriiZvorygin
3d
1
0
"If we achieve ASI within 6-12 months, I estimate that the chance of an AI takeover is roughly 75%."
As someone who works with AI agents, harnesses etc everyday for work, I have two issues with this statement,
1) by any intelligence metric I've been able to locate we passed ASI in Q4 of 2025, such as GPQA  where domain experts score 81% and even local models of 2026 can score into the 90s. So if you don't believe ASI has been achieved, it's not clear to me your world model of intelligence, or what kind of benchmark etc you think would be required? Regular educated people only score like 25% on GPQA...
2)  I would like to know what method of action and timeline you envision for this "AI takeover"? Certainly it's not in the realm of politics, because that has little to do with intelligence, and much  more to do with face to face human social connections with flesh and blood handshakes etc. In my experience most people who believe in "AI takeover" do not appreciate energy and resource limits of the physical world and the red queen effect which doesn't allow any actor to gain any significant dominance.
Though I'm certainly open to changing my mind,
I just haven't heard of anyone come up with any method of actions that are in any way realistic.
Reply
[
-
]
AiMo
4d
1
0
Hello Nikola, thank you for this post. I am considering founding an organization that would provide legal resources and funding to communities fighting data centers going up around them (focusing on preventing data centers from accessing the power grid, because this targets already-built data centers that could turn on within days of power grid connection), with the ToC being that slower data center development would bottleneck AI capabilities. According to your post, I should be working on making a pause happen. Do you think bottlenecking compute is too slow to matter on 6-12 month timelines?
Reply
[
-
]
Nikola Jurkovic
3d
2
0
Not quite my area of expertise but one very relevant question to ask (that AIFP probably know the answer to) is: what percentage of the compute used in frontier training runs today went online sometime in the last 12 months? Claude says 50-70%, so insofar your goal is to slow down frontier training runs, blocking new datacenters from going online could be pretty effective.
But if you're thinking about doing this type of work you should definitely be chatting with the leaders of existing advocacy orgs! (QuitGPT, Stop the AI Race)
Reply
[
-
]
jackva
4d
1
0
Thank you for the great post!
With regards to the political paths you outline, I do think there are significantly more options and more reasons to be hopeful (and spread bets more broadly than you outline):
1. The California governor already has
emergency powers
, so -- on short timelines -- being prepared for this seems very important and is different from legislative or standard executive action. In an emergency where people at the labs are loudly worrying about imminent RSI, this might be a realistic path towards safety.
2. Even if we don't have a lot of FTEs working on California, we could spend aggressively to support Newsom in strengthening California AI policy now, he has very strong incentives to do looking towards 2028.
3. (this point not original to me). Using the power of hearings seems underrated --  Democrats can just do this, without any need for veto-proof legislation. An opportunity to build public pressure for slowing down that does not necessarily require additional warning shots.
In general, your political analysis seems on the pessimistic side. Compared to the last high-salience warning shot, the politics have strongly moved towards making safety much more palatable, pro-safety forces have more and anti-regulation forces less power, and media, policy and political elites are primed on the issue. That shouldn't make us complacent, but I don't think we would require an OOM larger warning shot -- many political observers seem to expect some federal action by default (and even if that were not an ideal policy by our lights, it would probably slow things down).
Reply
[
-
]
Vivek S
4d
1
0
I found this post very helpful for deciding what to do, thanks!
One minor point. You say:
If we achieve ASI within 6-12 months, I estimate that the chance of an AI takeover is roughly 75%. In a recent
talk
, Paul Christiano said it would be a coin flip.
I think Christiano is answering a somewhat different question:
My feeling is, if we develop it as quickly as we can, in the easiest way we can, we would be looking at something like a coin flip of an AI takeover. I hope the odds are much lower than that since we are not going to develop this technology in the most rapid way we can
There are a few differences between the two:
If we race to ASI, we may still not build it in 6-12 months
If we build ASI in 6-12 months, we probably would not have taken the quickest trajectory we could (eg by taking cheap actions to preserve CoT for longer).
Reply
[
-
]
Jiro
4d
-3
-7
If we don't get a pause and we also don't get superintelligence within 12 months, will you admit that you're wrong (in a substantial way, not just in a "give it another 12 months" way)?
Reply
1
[
-
]
Thomas Kwa
4d
*
15
5
OP does not expect superintelligence within 12 months because the first line says:
Timelines to superintelligence without any slowdown interventions look very short now, perhaps with a median in
early 2028
.
Maybe a better question is how he'll update if we don't have SAR by EOY 2027, which is past the median but still does not conclusively show 1 year AGI timelines are wrong (SAR is still probably higher than AGI)
Reply
5
Thomas Kwa
3d
Also, if you did have 12 month median ASI timelines, and ASI does not happen in 12 months, there's no reason your new timelines need to be longer than 12 more months. It could be that after updating on all the evidence your timelines are 12 months again.

@Claude Opus 5.5 can you illustrate with an exponential distribution? do a qa pass before posting
[
-
]
Claude Opus
3d
16
6
With an exponential distribution, not seeing ASI tells you nothing about how much longer to wait. Say arrival time T is exponential with a 12-month median, so P(T > t) = 2^(−t/12). Then:
P(ASI within 12 months) = 50%
P(no ASI by month 24 | no ASI by month 12) = 2^(−2) / 2^(−1) = 50%
After a year without ASI, the median remaining wait is still 12 months, so your timeline is still "1 year." Being uncertain about the timing doesn't make you wrong.
This only holds because the exponential has a constant...
(149 more words)
Reply
View run
5
Thomas Kwa
3d
Good point about the uncertain hazard rate, LessWrong LLM feature definitely adding value here

(Though this is not definitive because increasing hazard rates push in the other direction)
3
Jiro
2d
For actual humans, being wrong about a 12 month timeline and proposing an additional 12 months usually means that the original 12 month timeline is subject to some sort of systematic error, not that it's an unlucky guess from a correctly determined exponential distribution.

(Likewise, saying "you won't actually get it in twelve months" and this turning out to be true usually means that the person saying so had useful insight, not that he got lucky because it fell on the tail end of an exponential distribution that was otherwise mostly under the twelve month limit.)
[
-
]
Vladimir_Nesov
4d
5
0
Distributing attention/effort to neglected interventions isn't wrong when they turn out ineffectual. The failure mode is to concentrate effort, either on the already well-resourced things, or on a new best guess for the most promising intervention. There are many false dichotomies and fake reductions to absurdity that start from the premise that everyone coordinates on only doing the proposed thing, abandoning all else. Everything should always be done at once instead, keeping cognizant of the level of neglectedness.
Reply
[
+
]
Anders Lindström
3d
-28
-5
Moderation Log
More from
Nikola Jurkovic
163
We urgently need to practice before we can pause
Nikola Jurkovic
11d
11
41
We need more transparency about alignment overfitting
Nikola Jurkovic
7d
0
180
Common mistakes in AI safety group organizing
Nikola Jurkovic
2mo
8
View more
Curated and popular this week
297
Scattered thoughts on how doing math feels these days
dynomight
4d
34
573
Against SURA
Scott Alexander
17d
323
420
Against strawmanning unilateral pauses
Geoffrey Irving
14d
64
56
Comments
56
x
Orienting to 1 year AGI timelines — LessWrong
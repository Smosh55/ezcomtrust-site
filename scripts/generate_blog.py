# -*- coding: utf-8 -*-
"""
Generates the EZ Comtrust blog: blog/index.html + one page per post.
Run:  python scripts/generate_blog.py
Edit the AUTHORS / POSTS data below and re-run to regenerate.
"""
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BLOG_DIR = os.path.join(ROOT, "blog")

PHONE = "347-893-6504"
TEL = "+13478936504"

AUTHORS = {
    "david":  ("David Katz", "DK", "Founder &amp; Principal Consultant",
               "David founded EZ Comtrust to bring enterprise-grade IT to long-term care. He has spent more than 15 years keeping healthcare systems secure, compliant, and online."),
    "sarah":  ("Sarah Nguyen", "SN", "Security &amp; Compliance Analyst",
               "Sarah helps facilities pass surveys and cyber-insurance reviews with documented, defensible HIPAA safeguards that hold up under scrutiny."),
    "michael":("Michael Torres", "MT", "Network Engineer",
               "Michael designs and tunes the networks and Wi-Fi that keep clinical systems connected across every wing and resident room."),
    "rachel": ("Rachel Green", "RG", "Client Success Manager",
               "Rachel makes sure every EZ Comtrust client gets more value, clearer bills, and fewer surprises from their technology spend."),
    "james":  ("James Miller", "JM", "Systems Administrator",
               "James manages servers, backups, and cloud systems so resident data is always available, recoverable, and protected."),
    "aaron":  ("Aaron Feldman", "AF", "vCIO &amp; Technology Strategist",
               "Aaron acts as an outsourced CIO for care facilities, aligning technology roadmaps with budgets, surveys, and cyber-insurance requirements."),
    "lena":   ("Lena Petrov", "LP", "Help Desk Team Lead",
               "Lena leads the support team that care staff reach on the first ring, and builds security training that respects their time."),
    "daniel": ("Daniel Cohen", "DC", "Field Services Technician",
               "Daniel installs and maintains the phones, cameras, and cabling that keep facilities running on the ground, day and night."),
}

def p(t):  return ("p", t)
def h2(t): return ("h2", t)
def ul(items): return ("ul", items)
def callout(t): return ("callout", t)

POSTS = [
 dict(slug="why-ransomware-targets-nursing-homes",
   title="Why Ransomware Targets Nursing Homes (and How to Lock It Out)",
   cat="Cybersecurity", author="sarah", date="June 18, 2026", read=6,
   excerpt="Long-term care has become a favorite target for ransomware crews. Here is why, and the practical layers that actually keep attackers out of resident data.",
   body=[
     p("Ransomware crews are not picking on nursing homes by accident. Long-term care facilities hold exactly what attackers want: sensitive protected health information, systems that cannot afford downtime, and IT environments that are often stretched thin. When charting has to keep moving and lives depend on it, the pressure to pay a ransom is enormous, and attackers know it."),
     h2("Why facilities are such attractive targets"),
     p("A hospital may have a dedicated security team. A 120-bed skilled nursing facility usually does not. Yet both hold similar data. That gap between the value of the data and the resources defending it is precisely what criminals look for."),
     ul(["Round-the-clock operations mean downtime is felt immediately, raising the pressure to pay.",
         "Staff turnover and shared workstations make phishing and password reuse common.",
         "Older devices and unpatched systems linger because replacing them mid-operation is disruptive.",
         "A single breach of PHI can trigger reportable events and steep penalties."]),
     h2("The layers that actually stop it"),
     p("There is no single product that makes a facility ransomware-proof. Real protection comes from layers, so that if one fails, the next one holds."),
     ul(["Managed detection and response that watches every endpoint 24/7 and isolates threats in real time.",
         "Multi-factor authentication on email, remote access, and your EHR.",
         "Immutable, tested backups that an attacker cannot encrypt or delete.",
         "Email filtering and ongoing phishing training for the people at the keyboard.",
         "Prompt patching of servers, workstations, and network gear."]),
     callout("The goal is not to be unbreakable. It is to make your facility a harder, slower target than the next one, and to recover in minutes if something does slip through."),
     p("If you are not sure which of these layers you have in place today, that uncertainty is itself the risk. A security assessment maps exactly where you stand and what to fix first."),
   ]),
 dict(slug="hipaa-risk-assessment-survey",
   title="HIPAA Risk Assessments: What Surveyors Actually Look For",
   cat="HIPAA &amp; Compliance", author="sarah", date="June 3, 2026", read=7,
   excerpt="A security risk assessment is required, but most facilities treat it as a checkbox. Here is what a real one contains and how it protects you at survey time.",
   body=[
     p("The HIPAA Security Rule requires a risk analysis. Many facilities have a dusty document from years ago and assume they are covered. They are not. A risk assessment is meant to be a living picture of where protected health information lives, how it flows, and where it is exposed."),
     h2("It starts with where PHI actually lives"),
     p("You cannot protect what you have not mapped. A proper assessment inventories every place resident data is created, stored, or transmitted: the EHR, workstations, mobile devices, email, backups, faxes, and any third-party vendor with access."),
     h2("What reviewers and insurers expect to see"),
     ul(["A current inventory of systems and the PHI they touch.",
         "Documented technical safeguards: encryption, access controls, and multi-factor authentication.",
         "Evidence of monitoring and how you detect and respond to incidents.",
         "Staff security awareness training records.",
         "A prioritized remediation plan with owners and dates, not just a list of problems."]),
     callout("The single most common gap we find is not a missing firewall. It is missing documentation of the safeguards a facility already has. If it is not written down, at survey time it did not happen."),
     h2("Turning it into an ongoing program"),
     p("A risk assessment is not an annual event you survive and forget. The strongest facilities revisit it whenever they add a system, change a vendor, or renew cyber-insurance. That cadence turns compliance from a scramble into a routine, and it means you are never caught explaining a gap you already knew about."),
     p("Done right, the assessment becomes your evidence file: the thing you hand a surveyor or insurer that answers their questions before they finish asking."),
   ]),
 dict(slug="signs-facility-wifi-hurting-care",
   title="5 Signs Your Facility Wi-Fi Is Hurting Resident Care",
   cat="Connectivity", author="michael", date="May 27, 2026", read=5,
   excerpt="Slow or spotty Wi-Fi is not just annoying. In a care setting it delays charting, drops calls, and frustrates families. Here are the warning signs.",
   body=[
     p("In a nursing home, Wi-Fi is not a convenience. It carries clinical charting, medication carts, VoIP phones, cameras, and family video calls. When it is weak, resident care slows down in ways that are easy to miss until you know the signs."),
     h2("1. Charting stalls in certain rooms"),
     p("If nurses know which rooms and hallways to avoid because the cart loses signal, you do not have a coverage problem in theory. You have one in practice, and it is costing time at the point of care."),
     h2("2. Calls and video drop when people move"),
     p("VoIP handsets and tablets that cut out as staff walk between wings usually point to gaps in access-point coverage or poor roaming between them."),
     h2("3. Everything slows down at shift change"),
     p("When many devices connect at once and the network crawls, your access points or internet circuit are undersized for real usage."),
     h2("4. Guest and clinical traffic share one network"),
     p("If residents, families, and clinical systems all ride the same flat network, you have both a performance problem and a serious security exposure."),
     h2("5. Nobody can say where the dead zones are"),
     ul(["No recent wireless survey on file.",
         "Access points mounted wherever there happened to be a cable, not where coverage is needed.",
         "Complaints treated one at a time instead of mapped."]),
     callout("A professional Wi-Fi survey turns guesswork into a heat map. You see exactly where coverage fails and what it takes to fix it, before it affects another shift."),
   ]),
 dict(slug="wifi-installation-optimization-multi-wing",
   title="Wi-Fi Installation and Optimization for Multi-Wing Facilities",
   cat="Connectivity", author="michael", date="May 14, 2026", read=6,
   excerpt="Reliable wireless across a sprawling building is an engineering job, not a matter of adding another router. Here is how we design and tune it.",
   body=[
     p("Covering a single office with Wi-Fi is easy. Covering a multi-wing care facility, with thick walls, long corridors, metal med carts, and hundreds of moving devices, is a different discipline. Adding a bigger router rarely fixes it. Proper design does."),
     h2("It begins with a survey, not a guess"),
     p("Before we mount anything, we survey the building to measure signal, interference, and the real-world obstacles between where people work and where coverage comes from. That produces a coverage map and a plan, so access points go where they are needed rather than where a cable happened to reach."),
     h2("Designing for how care actually moves"),
     ul(["Enough access points, correctly placed, so there are no dead zones in rooms or hallways.",
         "Seamless roaming so a phone or cart stays connected as staff walk from wing to wing.",
         "Separate networks for clinical systems, staff, and guests, so a family streaming video never competes with charting.",
         "Capacity planned for peak times like shift change, not just a quiet afternoon."]),
     h2("Optimization is ongoing, not one and done"),
     p("Buildings change. New equipment, new walls, and new neighbors on nearby channels all affect performance. We monitor the wireless network and tune channels and power over time, so the coverage you paid for on day one is still there a year later."),
     callout("Good Wi-Fi is invisible. Staff never think about it because it simply works, in every room, on every shift. That is the goal of a proper installation and ongoing optimization."),
     p("If your facility has grown wing by wing and the wireless has never been designed as a whole, a survey is the fastest way to find out what is really going on."),
   ]),
 dict(slug="ehr-downtime-plan",
   title="EHR Downtime: Build the Plan Before You Need It",
   cat="EHR", author="james", date="May 2, 2026", read=6,
   excerpt="EHR outages happen. What separates a minor hiccup from a crisis is whether you planned for it. Here is what a real downtime plan includes.",
   body=[
     p("Your electronic health record will go down at some point. The internet circuit fails, the platform has an outage, or a workstation dies mid-shift. The facilities that stay calm are the ones that decided what to do long before it happened."),
     h2("Why paper alone is not a plan"),
     p("Everyone says they will fall back to paper. But if nobody knows where the downtime forms are, who to call, or how charting gets reconciled afterward, that fallback creates its own risk of errors and gaps."),
     h2("What a real downtime plan covers"),
     ul(["Clear roles: who declares downtime, who notifies staff, who contacts IT and the vendor.",
         "Accessible downtime documentation forms that do not live only on the system that is down.",
         "A known process for reconciling paper charting back into the EHR afterward.",
         "Redundant internet, so a single circuit failure does not take the EHR offline.",
         "Verified backups and a tested recovery time, so you know how long a full restore actually takes."]),
     callout("The best time to test your downtime plan is a quiet Tuesday, not during an actual outage. A short tabletop exercise reveals the gaps while the stakes are low."),
     h2("Prevention still matters most"),
     p("A plan handles the outage you cannot prevent. Proactive monitoring, redundant connectivity, and maintained hardware prevent most of the ones you can. Together they turn EHR downtime from a crisis into a manageable, rehearsed event."),
   ]),
 dict(slug="cost-of-we-have-a-guy-it",
   title="The Real Cost of 'We Have a Guy' IT in Long-Term Care",
   cat="Strategy", author="david", date="April 22, 2026", read=5,
   excerpt="A part-time technician or a nephew who is good with computers feels cheap until something breaks at 2 a.m. Here is the hidden bill.",
   body=[
     p("Plenty of facilities run on informal IT: a part-time technician, a vendor who shows up when called, or a staff member who is handy with computers. It feels economical. In long-term care, it usually is not, and the cost shows up at the worst possible moment."),
     h2("Break-fix means you only pay attention after it breaks"),
     p("The informal model is reactive by design. Nobody is watching the systems until something fails, which means small problems grow into outages, and outages happen on nights and weekends when your guy is unreachable."),
     h2("The hidden bill"),
     ul(["Downtime during which staff revert to paper and errors climb.",
         "Security gaps that go unnoticed until a breach forces the issue.",
         "No documentation, so when your guy leaves, the knowledge leaves with them.",
         "Compliance exposure because no one is maintaining or documenting safeguards.",
         "Staff time lost to problems that a monitored environment would have caught early."]),
     callout("The question is not what managed IT costs. It is what one ransomware incident, one failed survey, or one week of EHR instability costs, and how much of that a flat monthly partnership would have prevented."),
     h2("What predictable looks like"),
     p("A managed partner watches your systems around the clock, documents everything, keeps safeguards current, and charges one flat monthly rate. You trade unpredictable emergencies for a predictable line item, and you get a team instead of a single point of failure."),
   ]),
 dict(slug="printer-copier-leases-managed-print",
   title="Printer and Copier Leases: Stop Overpaying for Managed Print",
   cat="Hardware", author="rachel", date="April 9, 2026", read=5,
   excerpt="Facilities quietly bleed money on printing: toner runs, service calls, and aging machines. A managed lease turns it into one predictable bill.",
   body=[
     p("Printing is one of those costs nobody watches. Toner gets ordered in a panic, an aging copier jams during morning charting, and a separate invoice arrives every time a technician visits. Add it up across a year and it is real money, spent unpredictably."),
     h2("Why a lease usually beats buying"),
     p("Buying a copier outright means a large upfront cost and a machine that is your problem when it ages or breaks. A managed lease spreads the cost, keeps the equipment current, and bundles the things that usually surprise you."),
     ul(["Multifunction printers and copiers sized to each area of the facility.",
         "Toner and supplies included, so nobody is scrambling at month end.",
         "Service and repairs covered, not billed per visit.",
         "Usage monitoring, so you can see and control what is actually being printed.",
         "One predictable monthly bill instead of scattered charges."]),
     h2("The compliance angle people forget"),
     p("Modern copiers store images of what they scan and print on internal drives. In a facility handling protected health information, that matters. Managed print includes securing and wiping those devices, so a returned or retired copier does not walk out the door with resident data on it."),
     callout("If you cannot say what your facility spent on printing last year, that is the first sign a managed lease will save you money and headaches."),
     p("We review your current fleet and usage, then propose a lease that covers the machines, supplies, and service for one flat rate, with the security piece handled by default."),
   ]),
 dict(slug="voip-phones-for-nurses",
   title="VoIP Phone Systems That Fit How Nurses Actually Work",
   cat="Communications", author="daniel", date="March 30, 2026", read=5,
   excerpt="A phone system for a care facility has to survive shift changes, reach the right station instantly, and never drop a family call. Here is what to look for.",
   body=[
     p("A phone system in a nursing home is not a back-office convenience. It is how families reach loved ones, how staff coordinate across wings, and how the front desk manages a constant flow of calls. When it is clunky, everyone feels it. Modern VoIP fixes most of the old frustrations, if it is set up for how care actually works."),
     h2("What matters in a care setting"),
     ul(["Reliable coverage on wireless handsets that move with staff across the building.",
         "Smart call routing so calls reach the right station or department the first time.",
         "Voicemail-to-email so messages are not trapped on a single handset.",
         "Clear call quality that holds up during busy periods.",
         "Simple administration so adding a phone or changing a route does not require a specialist."]),
     h2("Why VoIP, and why now"),
     p("Traditional phone lines are expensive and inflexible. VoIP runs over your network, which means lower monthly costs, easier moves and changes, and features that used to require costly hardware. The catch is that it depends on a healthy network, which is exactly why phones, Wi-Fi, and cabling should be handled by one partner rather than three."),
     callout("A dropped family call or a front desk that cannot transfer to the right wing is not a phone problem. It is a design problem, and it is fixable."),
     p("We design VoIP around your floor plan and staffing, then support it alongside the network it runs on, so the phones and the Wi-Fi never point fingers at each other."),
   ]),
 dict(slug="hipaa-compliant-efax",
   title="HIPAA-Compliant eFax: Retire the Fax Machine Safely",
   cat="Communications", author="sarah", date="March 19, 2026", read=5,
   excerpt="Healthcare still runs on faxes, but the machine in the hallway is a compliance liability. HIPAA-compliant eFax keeps the workflow and drops the risk.",
   body=[
     p("Faxing refuses to die in healthcare. Pharmacies, physicians, and referrals still depend on it. The problem is the physical machine sitting in a hallway, printing protected health information onto a tray anyone can walk past. There is a better way that keeps the workflow everyone relies on."),
     h2("Why the old fax machine is a liability"),
     ul(["Documents with PHI sit in an output tray in a shared space.",
         "There is no audit trail of who sent or received what.",
         "Misdials send resident information to the wrong number with no encryption.",
         "A dedicated phone line and hardware cost money to maintain."]),
     h2("How HIPAA-compliant eFax works"),
     p("Digital faxing sends and receives through secure, encrypted services tied to your email or a web portal. Faxes arrive as protected documents on a specific person's screen, not on a public tray, and every send and receive is logged."),
     ul(["Encryption in transit and at rest.",
         "Audit trails that document every transmission.",
         "Faxes routed to the right person, not a shared machine.",
         "No dedicated fax line or hardware to maintain."]),
     callout("You keep the exact workflow your partners expect, a fax number they can send to, while removing the hallway machine and the compliance exposure that comes with it."),
     p("Retiring the fax machine is one of the easiest compliance wins a facility can make, and staff rarely miss it once secure eFax is in place."),
   ]),
 dict(slug="backup-disaster-recovery-321",
   title="Backup and Disaster Recovery: The 3-2-1 Rule for Care Facilities",
   cat="Managed IT", author="james", date="March 6, 2026", read=6,
   excerpt="Backups feel handled until you need to restore and discover they were failing for months. The 3-2-1 rule, applied to healthcare, prevents that.",
   body=[
     p("Everyone has backups until the day they need them. That is when facilities discover the job had been silently failing, the backup was never tested, or ransomware encrypted the backups along with everything else. In long-term care, where resident data must be available and recoverable, that discovery is a disaster."),
     h2("The 3-2-1 rule, explained"),
     ul(["Three copies of your data: the live copy plus two backups.",
         "Two different types of storage, so one failure does not take out both.",
         "One copy kept off-site, protected from a fire, flood, or local ransomware event."]),
     h2("What healthcare adds to the rule"),
     p("For a care facility, three-two-one is the floor, not the ceiling. Resident data demands a few things more."),
     ul(["Encryption, so a stolen or intercepted backup is useless to anyone else.",
         "Immutability, so an attacker who gets in cannot alter or delete the backups.",
         "Verified restores, so you know the backup actually works before you need it.",
         "A known recovery time, so you can answer how long a full restore really takes."]),
     callout("A backup you have never restored is a hope, not a plan. We test restores on a schedule so that recovery is a routine we have already rehearsed."),
     h2("Recovery is the real test"),
     p("The point of backup is not storage. It is getting your facility back online quickly after the worst happens. That is why we measure success by recovery time, not by whether a job says it completed."),
   ]),
 dict(slug="security-cameras-resident-safety",
   title="Security Cameras and Resident Safety: A Practical Buyer's Guide",
   cat="Hardware", author="daniel", date="February 24, 2026", read=6,
   excerpt="Cameras support resident safety, deter incidents, and settle disputes, but only if they are designed and placed correctly. Here is how to get it right.",
   body=[
     p("A camera system in a care facility does more than record. Done well, it deters problems, supports resident and staff safety, and provides a clear record when questions arrive from families or investigators. Done poorly, it is a wall of blurry footage nobody can use when it matters."),
     h2("Where cameras belong, and where they do not"),
     p("Coverage should focus on entrances, exits, hallways, and common areas: the places where safety and accountability matter most. Resident privacy in personal spaces has to be respected, which is why placement is a design decision, not a matter of mounting cameras everywhere."),
     h2("What separates a useful system from a useless one"),
     ul(["Enough resolution to actually identify people and events, not just see motion.",
         "Coverage of entrances and exits so you know who comes and goes.",
         "Reliable recording and enough retention to look back when an issue surfaces days later.",
         "Secure remote viewing, so administrators can check in without standing at a monitor.",
         "Proper network design, so cameras do not choke clinical traffic."]),
     callout("Cameras share the same network and cabling as your other systems. Treating them as a separate island is how facilities end up with security footage that slows down charting."),
     h2("One partner for cameras, cabling, and network"),
     p("Because cameras depend on cabling and the network, it makes sense to have the same team install and support all three. That is how you avoid the finger-pointing that happens when the camera vendor blames the network and the network vendor blames the cameras."),
   ]),
 dict(slug="low-voltage-cabling-foundation",
   title="Low-Voltage Cabling: The Foundation Nobody Sees",
   cat="Hardware", author="michael", date="February 12, 2026", read=5,
   excerpt="Every reliable network, phone, and camera system rests on cabling done right. When it is done wrong, everything above it suffers.",
   body=[
     p("Cabling is the least glamorous part of facility technology and the most consequential. It sits in the walls and ceilings, out of sight, until the day a flaky connection causes a phone to drop, a camera to freeze, or a workstation to lose its network. Everything you rely on rests on it."),
     h2("Why inherited wiring causes so many problems"),
     p("Many facilities have grown wing by wing over decades, and the cabling grew with them, often without a plan. The result is a tangle of mixed standards, undocumented runs, and connections that were never meant to carry today's traffic."),
     ul(["Runs that exceed length limits, causing intermittent, hard-to-diagnose failures.",
         "Undocumented cabling, so nobody knows what connects to what.",
         "Mixed or outdated standards that cannot support modern speeds.",
         "Cabling that is not done to code, which is both a performance and a safety issue."]),
     h2("What structured cabling gives you"),
     p("A properly designed cabling system is documented, labeled, tested, and built to standard. It supports your network, phones, and cameras today and leaves room to grow. When something does go wrong, it can be traced and fixed in minutes instead of hours."),
     callout("Structured cabling is invisible when it is right. You only notice it when it is wrong, and by then it is affecting care."),
     p("Whether you are building new, renovating, or fixing the wiring you inherited, getting the foundation right is what makes everything above it dependable."),
   ]),
 dict(slug="mfa-without-staff-revolt",
   title="Multi-Factor Authentication Without the Staff Revolt",
   cat="Cybersecurity", author="lena", date="February 3, 2026", read=5,
   excerpt="MFA is one of the highest-impact security controls you can add, and one of the most resisted. Here is how to roll it out without slowing care.",
   body=[
     p("Multi-factor authentication stops the vast majority of account takeovers, which makes it one of the best security investments a facility can make. It is also the change staff push back on hardest, because anything that adds a step at the keyboard feels like friction during a busy shift. Both things are true, and both can be managed."),
     h2("Why MFA matters so much"),
     p("Passwords get reused, phished, and guessed. MFA means that even a stolen password is not enough to get in. For email, remote access, and the EHR, that single control blocks attacks that would otherwise succeed."),
     h2("Rolling it out without the revolt"),
     ul(["Start with the highest-risk accounts: email, remote access, and administrators.",
         "Choose methods that fit the workflow, like app prompts or badges, not clumsy code entry on shared devices.",
         "Use trusted devices and sensible session lengths so staff are not prompted constantly.",
         "Explain the why in plain terms: it protects residents, and it protects them personally.",
         "Roll out in stages, with support on hand, rather than flipping a switch overnight."]),
     callout("Resistance to MFA is almost always about how it was deployed, not about MFA itself. Thoughtful rollout turns a source of complaints into a control nobody thinks about."),
     h2("The insurance angle"),
     p("Cyber-insurance carriers increasingly require MFA to issue or renew a policy. Putting it in place is no longer just good practice. It is often the difference between being insurable and not."),
   ]),
 dict(slug="cyber-insurance-renewal-questionnaire",
   title="Cyber Insurance Renewals: The Questionnaire That Trips Up Facilities",
   cat="Compliance", author="aaron", date="January 27, 2026", read=6,
   excerpt="Cyber-insurance applications now read like a security audit. Answer them wrong and you risk denial or a claim that will not pay. Here is how to be ready.",
   body=[
     p("Cyber-insurance used to be a quick form and a premium. Not anymore. Today's applications ask detailed questions about your security controls, and the answers matter twice: once to get coverage at a reasonable rate, and again if you ever file a claim and the carrier checks whether you actually had the controls you claimed."),
     h2("What the questionnaire really wants to know"),
     ul(["Do you have multi-factor authentication on email and remote access?",
         "Do you run managed detection and response or equivalent endpoint monitoring?",
         "Are your backups encrypted, tested, and kept offline or immutable?",
         "Do you train staff on phishing and security awareness?",
         "Do you patch systems promptly and have an incident response plan?"]),
     h2("Why honest answers matter more than perfect ones"),
     p("Overstating your controls to get a better rate is dangerous. If you claim MFA everywhere and a breach reveals you did not have it, the carrier can deny the claim. The goal is to genuinely have the controls, then document them so the answers are both true and defensible."),
     callout("We help facilities complete these questionnaires accurately, and just as importantly, we close the gaps the questions expose so the answers are yes for real."),
     h2("Turn the renewal into a checklist"),
     p("Instead of dreading the annual questionnaire, treat it as a free security checklist written by people who pay out when things go wrong. Each question points at a control worth having. Meet them, document them, and the renewal becomes routine."),
   ]),
 dict(slug="what-a-vcio-does",
   title="What a vCIO Does for a Nursing Home (and Why It Pays for Itself)",
   cat="Strategy", author="aaron", date="January 19, 2026", read=6,
   excerpt="A full-time CIO is out of reach for most facilities. A virtual CIO gives you the strategy without the salary. Here is what that actually means.",
   body=[
     p("Large health systems have a chief information officer setting technology strategy. A single nursing home cannot justify that salary, so technology decisions often get made reactively, one emergency at a time. A virtual CIO, or vCIO, fills that gap: senior strategy on a fractional basis."),
     h2("Beyond fixing what breaks"),
     p("Day-to-day support keeps things running. A vCIO looks further ahead. The role is about making sure your technology serves the facility's goals, budget, and compliance obligations, rather than lurching from one surprise to the next."),
     h2("What a vCIO actually does"),
     ul(["Builds a technology roadmap tied to your budget, so upgrades are planned, not emergencies.",
         "Reviews security and compliance posture and prioritizes what to address first.",
         "Plans hardware refreshes before equipment fails, not after.",
         "Evaluates vendors and new systems so you are not sold things you do not need.",
         "Translates technology into plain business terms for ownership and administration."]),
     callout("The value of a vCIO shows up as problems that never happen: the outage you prevented, the survey you passed, the purchase you did not waste money on."),
     h2("Why it pays for itself"),
     p("Planned technology is cheaper than reactive technology. A roadmap avoids the premium you pay for emergency replacements, the cost of downtime, and the money lost on tools that do not fit. For most facilities, the vCIO relationship pays for itself in avoided problems alone."),
   ]),
 dict(slug="phishing-training-that-sticks",
   title="Phishing Training That Actually Sticks for Busy Care Staff",
   cat="Cybersecurity", author="lena", date="January 12, 2026", read=5,
   excerpt="Most phishing attacks succeed because someone clicked. Training works, but only if it respects how little spare time care staff have. Here is how.",
   body=[
     p("The most sophisticated security stack in the world can be undone by one click on one convincing email. That is why staff are both the biggest risk and the best defense. The trick is training that actually changes behavior without pulling nurses away from residents for hours."),
     h2("Why one big annual session fails"),
     p("A long training video once a year is forgotten by the next week. Attackers do not attack once a year. Effective training is short, frequent, and tied to real examples staff would actually see."),
     h2("What works in a care setting"),
     ul(["Short, regular lessons that fit into a shift, not hour-long marathons.",
         "Simulated phishing emails that safely show who is at risk, without blame.",
         "Real examples relevant to healthcare: fake EHR logins, payroll scams, vendor invoices.",
         "Quick, judgment-free reporting so staff flag suspicious email instead of hiding a click.",
         "Positive reinforcement, because fear makes people hide mistakes rather than report them."]),
     callout("The goal is a culture where reporting a suspicious email is normal and fast. A reported phish is a stopped attack. A hidden click is a breach in progress."),
     h2("Measuring what matters"),
     p("Good training programs track whether click rates fall and reporting rates rise over time. Those two numbers, moving in the right direction, are what tell you the training is working, not whether everyone watched a video."),
   ]),
 dict(slug="microsoft-365-long-term-care",
   title="Microsoft 365 for Long-Term Care, Configured the Right Way",
   cat="Managed IT", author="james", date="January 6, 2026", read=6,
   excerpt="Most facilities use Microsoft 365 but leave it configured out of the box, which means insecure and unprotected. Here is what proper setup looks like.",
   body=[
     p("Microsoft 365 runs email, files, and collaboration for a huge share of care facilities. The problem is that most of them use it exactly as it arrived, with default settings that are not built for protecting health information. The tools to do it right are included. They just have to be turned on and configured."),
     h2("Default is not secure"),
     p("Out of the box, 365 does not enforce multi-factor authentication, does not retain data the way a healthcare organization needs, and leaves sharing wide open. Each of those is a gap that a proper configuration closes."),
     h2("What proper setup includes"),
     ul(["Multi-factor authentication enforced across all accounts.",
         "Email filtering and anti-phishing tuned beyond the defaults.",
         "Sharing and access controls locked down so files are not exposed by accident.",
         "Audit logging enabled, so you can see what happened if you ever need to.",
         "Third-party backup, because Microsoft's default retention is not a backup."]),
     callout("The most common misunderstanding we correct is that Microsoft backs up your data for you. It does not, at least not the way compliance requires. That is on you, and it is easily solved."),
     h2("Getting there without disruption"),
     p("Tightening 365 does not have to interrupt staff. Changes are staged, communicated, and supported, so the environment gets meaningfully more secure while the people using it barely notice, except that it now protects them."),
   ]),
 dict(slug="cut-telecom-utility-costs",
   title="Cutting Telecom and Utility Costs Without Cutting Service",
   cat="Strategy", author="rachel", date="December 18, 2025", read=5,
   excerpt="Facilities routinely overpay for internet, phone, and utilities on old contracts nobody revisits. A cost review finds the savings without cutting anything.",
   body=[
     p("Telecom and utility bills have a way of going on autopilot. A contract gets signed, the invoice arrives every month, and years pass without anyone checking whether the rate still makes sense. Meanwhile prices, technology, and your actual usage have all changed. That gap is money left on the table."),
     h2("Where the overspend hides"),
     ul(["Internet and phone contracts renewing automatically at outdated rates.",
         "Circuits and lines you are paying for but no longer use.",
         "Services that could be delivered more cheaply with newer technology, such as VoIP replacing old phone lines.",
         "Utility rates that were never shopped against alternatives."]),
     h2("How a cost review works"),
     p("A review is straightforward. We audit your current internet, phone, and utility bills, compare them against current market rates and your real usage, then shop and negotiate on your behalf. You see exactly what you are paying for and what it could cost instead."),
     callout("Cutting cost does not mean cutting service. Most savings come from paying a fair rate for what you already have, and from retiring things you stopped using long ago."),
     h2("Savings that fund other improvements"),
     p("The money a cost review frees up is often enough to fund the security or connectivity upgrades a facility has been putting off. It is one of the few projects that pays for itself immediately, and then keeps paying."),
     p("You keep the savings. We simply find them, and handle the shopping and negotiating so your team does not have to."),
   ]),
]

# ---------- templates ----------
def aurora():
    return ('<div class="hero__aurora" aria-hidden="true">'
            '<span class="blob blob--1"></span><span class="blob blob--2"></span>'
            '<span class="blob blob--3"></span><span class="blob blob--4"></span></div>')

def head(title, desc, rel):
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<meta name="theme-color" content="#0a1440" />
<title>{title}</title>
<meta name="description" content="{desc}" />
<link rel="icon" type="image/png" href="{rel}assets/icon.png" />
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@500;600;700;800&family=Inter:wght@400;500;600&display=swap" rel="stylesheet" />
<link rel="stylesheet" href="{rel}styles.css" />
</head>
<body>'''

def header(rel):
    return f'''
<div class="topbar">
  <div class="container topbar__inner">
    <span class="topbar__item">Managed IT &amp; technology for nursing homes and long-term care</span>
    <div class="topbar__right">
      <a href="tel:{TEL}" class="topbar__link"><svg class="ic" viewBox="0 0 24 24"><path d="M6.6 10.8a15 15 0 0 0 6.6 6.6l2.2-2.2a1 1 0 0 1 1-.24 11.4 11.4 0 0 0 3.6.58 1 1 0 0 1 1 1V20a1 1 0 0 1-1 1A17 17 0 0 1 3 4a1 1 0 0 1 1-1h3.5a1 1 0 0 1 1 1 11.4 11.4 0 0 0 .58 3.6 1 1 0 0 1-.24 1Z"/></svg> {PHONE}</a>
      <a href="mailto:info@ezcomtrust.com" class="topbar__link topbar__link--hide"><svg class="ic" viewBox="0 0 24 24"><path d="M3 5h18v14H3z"/><path d="m3 6 9 7 9-7"/></svg> info@ezcomtrust.com</a>
    </div>
  </div>
</div>
<header class="header" id="header">
  <div class="container header__inner">
    <a href="{rel}index.html" class="brand" aria-label="EZ Comtrust home">
      <img src="{rel}assets/icon.png" class="brand__mark" alt="" />
      <span class="brand__word">EZ&nbsp;Comtrust</span>
    </a>
    <nav class="nav" id="nav" aria-label="Primary">
      <a href="{rel}index.html#services" class="nav__link">Services</a>
      <a href="{rel}index.html#industry" class="nav__link">Why Nursing Homes</a>
      <a href="{rel}index.html#compliance" class="nav__link">HIPAA &amp; Security</a>
      <a href="./" class="nav__link">Blog</a>
      <a href="tel:{TEL}" class="nav__call">{PHONE}</a>
      <a href="{rel}index.html#contact" class="btn btn--primary nav__cta">Free Assessment</a>
    </nav>
    <button class="hamburger" id="hamburger" aria-label="Open menu" aria-expanded="false">
      <span></span><span></span><span></span>
    </button>
  </div>
</header>'''

def footer(rel):
    return f'''
<footer class="footer">
  <div class="container footer__inner">
    <div class="footer__brand">
      <div class="footer__logo">
        <img src="{rel}assets/icon.png" class="fl-mark" alt="EZ Comtrust icon" />
        <span class="fl-text">COMTRUST</span>
      </div>
      <p>Managed IT and technology built for nursing homes and long-term care. Trusted systems, so your team can focus on care.</p>
      <a href="tel:{TEL}" class="footer__phone">{PHONE}</a>
    </div>
    <div class="footer__col">
      <h4>Services</h4>
      <a href="{rel}index.html#services">Managed IT &amp; Help Desk</a>
      <a href="{rel}index.html#services">Cybersecurity</a>
      <a href="{rel}index.html#services">Wi-Fi &amp; Connectivity</a>
      <a href="{rel}index.html#services">Phones, Cameras &amp; Cabling</a>
      <a href="{rel}index.html#compliance">HIPAA Compliance</a>
    </div>
    <div class="footer__col">
      <h4>Company</h4>
      <a href="{rel}index.html#industry">Why Nursing Homes</a>
      <a href="{rel}index.html#process">How It Works</a>
      <a href="./">Blog</a>
      <a href="{rel}index.html#contact">Free Assessment</a>
    </div>
    <div class="footer__col">
      <h4>Get in touch</h4>
      <a href="tel:{TEL}">{PHONE}</a>
      <a href="mailto:info@ezcomtrust.com">info@ezcomtrust.com</a>
      <a href="https://www.ezcomtrust.com">www.ezcomtrust.com</a>
      <a href="{rel}index.html#contact" class="btn btn--primary btn--sm">Free Assessment</a>
    </div>
  </div>
  <div class="footer__bar">
    <div class="container footer__bar-inner">
      <span>&copy; 2026 EZ Computer Trust (EZ Comtrust). All rights reserved.</span>
      <span>HIPAA-aligned managed IT for long-term care.</span>
    </div>
  </div>
</footer>
<a href="tel:{TEL}" class="callbar" aria-label="Call EZ Comtrust">
  <svg class="ic" viewBox="0 0 24 24"><path d="M6.6 10.8a15 15 0 0 0 6.6 6.6l2.2-2.2a1 1 0 0 1 1-.24 11.4 11.4 0 0 0 3.6.58 1 1 0 0 1 1 1V20a1 1 0 0 1-1 1A17 17 0 0 1 3 4a1 1 0 0 1 1-1h3.5a1 1 0 0 1 1 1 11.4 11.4 0 0 0 .58 3.6 1 1 0 0 1-.24 1Z"/></svg>
  Call {PHONE}
</a>
<script src="{rel}script.js"></script>
</body>
</html>'''

def render_body(blocks):
    out = []
    for kind, val in blocks:
        if kind == "p":
            out.append(f"<p>{val}</p>")
        elif kind == "h2":
            out.append(f"<h2>{val}</h2>")
        elif kind == "ul":
            lis = "".join(f"<li>{i}</li>" for i in val)
            out.append(f"<ul>{lis}</ul>")
        elif kind == "callout":
            out.append(f'<div class="callout"><p>{val}</p></div>')
    return "\n        ".join(out)

def card(post, rel_to_post):
    name, initials, role, bio = AUTHORS[post["author"]]
    return f'''<article class="pcard">
        <div class="pcard__body">
          <span class="tag">{post["cat"]}</span>
          <h2><a href="{rel_to_post}">{post["title"]}</a></h2>
          <p class="pcard__ex">{post["excerpt"]}</p>
          <div class="byline">
            <span class="avatar">{initials}</span>
            <span class="byline__meta">
              <span class="byline__name">{name}</span>
              <span class="byline__sub">{post["date"]} &middot; {post["read"]} min read</span>
            </span>
          </div>
        </div>
      </article>'''

def build_index():
    cards = "\n      ".join(card(pp, f'{pp["slug"]}.html') for pp in POSTS)
    html = head("Blog | EZ Comtrust | IT Insights for Nursing Homes",
                "Practical IT, cybersecurity, HIPAA, and connectivity insights for nursing homes and long-term care from the EZ Comtrust team.",
                "../")
    html += header("../")
    html += f'''
<main>
  <section class="bloghero">
    {aurora()}
    <div class="container bloghero__inner">
      <span class="eyebrow eyebrow--glow"><span class="dot"></span> The EZ Comtrust Blog</span>
      <h1>IT insights for <span class="hl">long-term care</span></h1>
      <p>Straight talk on cybersecurity, HIPAA, connectivity, and the technology that keeps nursing homes running, written by the people who do the work.</p>
    </div>
  </section>
  <section class="blogwrap">
    <div class="container">
      <div class="blog-grid">
      {cards}
      </div>
    </div>
  </section>
</main>'''
    html += footer("../")
    with open(os.path.join(BLOG_DIR, "index.html"), "w", encoding="utf-8") as f:
        f.write(html)

def build_post(i, post):
    name, initials, role, bio = AUTHORS[post["author"]]
    rel = "../"
    related = [POSTS[(i + k) % len(POSTS)] for k in (1, 2, 3)]
    rel_cards = "\n        ".join(card(rp, f'{rp["slug"]}.html') for rp in related)
    html = head(f'{post["title"]} | EZ Comtrust Blog',
                post["excerpt"].replace('"', "&quot;"), rel)
    html += header(rel)
    html += f'''
<main>
  <article>
    <header class="post-hero">
      {aurora()}
      <div class="container post-hero__inner">
        <span class="tag">{post["cat"]}</span>
        <h1>{post["title"]}</h1>
        <div class="post-meta">
          <span class="avatar">{initials}</span>
          <span class="post-meta__txt">
            <span class="post-meta__name">{name}</span>
            <span class="post-meta__sub">{role} &middot; {post["date"]} &middot; {post["read"]} min read</span>
          </span>
        </div>
      </div>
    </header>

    <div class="container">
      <div class="post-backrow"><a href="./" class="post-back">&larr; All articles</a></div>
    </div>

    <div class="article">
      <div class="container">
        <div class="article__inner">
          <div class="post-body">
        {render_body(post["body"])}
          </div>

          <div class="author-box">
            <span class="avatar">{initials}</span>
            <div>
              <div class="author-box__name">{name}</div>
              <div class="author-box__role">{role}</div>
              <p class="author-box__bio">{bio}</p>
            </div>
          </div>

          <div class="post-cta">
            {aurora()}
            <div class="post-cta__in">
              <h3>Want this handled for your facility?</h3>
              <p>Get a free IT and security assessment. We will map your risks, gaps, and quick wins, with no obligation.</p>
              <a href="{rel}index.html#contact" class="btn btn--primary btn--lg">Get my free assessment</a>
            </div>
          </div>

          <div class="readmore">
            <h3>More from the blog</h3>
            <div class="readmore__grid">
        {rel_cards}
            </div>
          </div>
        </div>
      </div>
    </div>
  </article>
</main>'''
    html += footer(rel)
    with open(os.path.join(BLOG_DIR, f'{post["slug"]}.html'), "w", encoding="utf-8") as f:
        f.write(html)

def main():
    os.makedirs(BLOG_DIR, exist_ok=True)
    build_index()
    for i, post in enumerate(POSTS):
        build_post(i, post)
    print(f"Generated blog/index.html + {len(POSTS)} posts in {BLOG_DIR}")

if __name__ == "__main__":
    main()

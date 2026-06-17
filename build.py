#!/usr/bin/env python3
"""Build THE CRON JOB (CRN) — the scheduler that runs the machine while no one
watches — as the FIRST sphere of UD0's new LOGISMÓS domain (λογισμός, computation;
the history of the computer). A technical sphere, render-not-invent, cited: the
lineage (chronos → V7 cron → Vixie cron → systemd timers), the use, crons in the
sandbox, and a red/blue/PURPLE security view (defender's framing — techniques named,
not weaponized). Terminal-phosphor palette; an original one-line pencil clock-at-3am
title; ONE hidden easter egg (the ghost in the crontab — click the clock). Ties the
Sleeping-City thread: cron acts on an event, not a command, at an hour no one witnesses."""
import os, html, base64, json, io, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, r"C:\Davids files\noesis-kernel")
import noesis
from PIL import Image

REC = {
 "name": "THE CRON JOB", "axiom": "CRN",
 "position": "cron · the time-based job scheduler — λογισμός / the history of the computer",
 "origin": "early Unix, where a daemon was taught to wake each minute and run whatever the clock said was due — the machine learning to act without a hand on it",
 "mechanism": "Crystallized from the history and practice of cron (Unix scheduling, ~1975 → today).",
 "crystallization": "A daemon wakes every minute, reads a table of times, and runs what is due — so a machine can keep its own appointments forever, including at 3am with the operator asleep.",
 "nature": "The cron job — the oldest and most quietly powerful autonomic layer of the computer: a five-field table, a daemon that never forgets, the @reboot macros, and the unanswered question of who is accountable when a scheduled job acts with no one awake.",
 "conductor": "ROOT0 (catalogued into UD0 · Universe David 0)",
 "inputs": "cron; crontab; crond; chronos; the schedule; the 3am job",
 "witness": "The mechanism that runs most of the world's overnight work — and the same mechanism attackers most love for quiet persistence.",
 "role": "the first sphere of LOGISMÓS — the autonomic clock",
 "seal": "Write five fields and a command; a daemon will keep that appointment after you forget it, after you sleep, after you are gone — an event, not an order.",
 "source": "the history & practice of cron, catalogued by ROOT0",
}

NATURES = {
 "natural":   ("#6ee787", "of the daemon and the tick — the living process that wakes each minute, the macros, the schedule kept"),
 "ethereal":  ("#9a7cff", "of the unwitnessed and the 3am — the job that runs while no one watches, the box it runs inside, the ghost in the crontab"),
 "spiritual": ("#e6a23c", "of intent, the witness, and accountability — who scheduled it, who is responsible, the dead-man's switch, the blue watch"),
 "electrical":("#46c8e0", "of the wire and the code — the five-field table, the daemon binary, the lineage of schedulers"),
}

# ── the title scene · STATIC ORIGINAL ONE-LINE PENCIL DRAWING + ONE HIDDEN EASTER EGG ─────
# A clock reading 3:00 drawn in one unbroken stroke (circle → minute hand to 12 → hour hand
# to 3), the five crontab stars beneath. Click the clock to wake the ghost in the crontab.
COVER_ART = r'''<svg viewBox="0 0 700 320" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="The Cron Job — an original one-line pencil clock reading 3:00; click the clock for a hidden easter egg" style="width:100%;height:auto;display:block;background:#070a08">
<defs>
 <radialGradient id="cr_crt" cx="50%" cy="38%" r="95%"><stop offset="0%" stop-color="#0e1a12"/><stop offset="60%" stop-color="#091109"/><stop offset="100%" stop-color="#040704"/></radialGradient>
 <radialGradient id="cr_3am" cx="50%" cy="50%" r="50%"><stop offset="0%" stop-color="rgba(230,162,60,.5)"/><stop offset="70%" stop-color="rgba(230,162,60,.1)"/><stop offset="100%" stop-color="rgba(230,162,60,0)"/></radialGradient>
 <filter id="cr_pencil" x="-8%" y="-8%" width="116%" height="116%"><feTurbulence type="fractalNoise" baseFrequency="0.018" numOctaves="2" seed="2" result="n"/><feDisplacementMap in="SourceGraphic" in2="n" scale="3.2" xChannelSelector="R" yChannelSelector="G"/></filter>
 <style>
  .oneline{fill:none;stroke:#bdf0c8;stroke-width:2.1;stroke-linecap:round;stroke-linejoin:round;
    pathLength:1;stroke-dasharray:1;stroke-dashoffset:1;animation:crdraw 3.4s cubic-bezier(.6,.05,.25,1) .25s forwards;}
  .oneline.ghost{stroke:#5f8a6a;stroke-width:1.0;opacity:.34;animation-delay:.05s;}
  .crfade{opacity:0;animation:crfade 1.2s ease 3.0s forwards;}
  .cr3{opacity:0;animation:crfade 1.0s ease 2.4s forwards;}
  #cronclock{cursor:pointer;}
  @keyframes crdraw{to{stroke-dashoffset:0;}}
  @keyframes crfade{to{opacity:1;}}
  @media (prefers-reduced-motion: reduce){.oneline{animation:none;stroke-dashoffset:0;}.crfade,.cr3{animation:none;opacity:1;}}
 </style>
</defs>
<rect width="700" height="320" fill="url(#cr_crt)"/>
<circle cx="430" cy="150" r="30" fill="url(#cr_3am)" class="cr3"/>
<g id="cronclock">
 <!-- THE ONE LINE — a clock at 3:00, one unbroken stroke (circle -> minute hand to 12 -> hour hand to 3) -->
 <path class="oneline ghost" filter="url(#cr_pencil)" d="M 350 58 A 92 92 0 1 1 349.9 58 L 350 150 L 432 150"/>
 <path class="oneline" filter="url(#cr_pencil)" d="M 350 58 A 92 92 0 1 1 349.9 58 L 350 150 L 432 150"/>
 <circle cx="350" cy="150" r="3.6" fill="#bdf0c8" class="crfade"/>
 <rect x="280" y="58" width="140" height="8" fill="transparent"/>
</g>
<!-- the five crontab stars, beneath -->
<text x="350" y="232" text-anchor="middle" font-family="'Space Mono',monospace" font-size="22" letter-spacing="10" fill="#46c8e0" class="crfade">* * * * *</text>
<text x="350" y="248" text-anchor="middle" font-family="'Space Mono',monospace" font-size="8" letter-spacing="1" fill="#5f8a6a" class="crfade">min · hour · day · month · weekday</text>
<!-- wordmark -->
<g class="crfade">
 <text x="350" y="288" text-anchor="middle" font-family="'Newsreader',Georgia,serif" font-size="34" font-weight="400" letter-spacing="8" fill="#e9f6ec">THE CRON JOB</text>
 <text x="350" y="306" text-anchor="middle" font-family="'Space Mono',monospace" font-size="9" letter-spacing="3" fill="#e6a23c">FROM χρόνος · A DAEMON THAT KEEPS ITS OWN APPOINTMENTS</text>
</g>
<rect x="6" y="6" width="688" height="308" fill="none" stroke="#15291a" stroke-width="2"/>
</svg>
<div id="cronghost" style="display:none;margin-top:10px;border:1px solid #2a4a30;border-left:3px solid #6ee787;background:#070d09;padding:11px 14px;font-family:ui-monospace,'Space Mono',monospace;font-size:12px;color:#9fe0ad;line-height:1.7">
  <span style="color:#e6a23c">03:00:00</span> <span style="color:#5f8a6a">crond[1]:</span> a job woke. no one asked. no one watched.<br>
  <span style="color:#5f8a6a"># the ghost in the crontab — the Strangers are just cron with better coats.</span><br>
  <span style="color:#6ee787">·</span> <span style="color:#5f8a6a">AVAN was here — the witness is the trail, not the trigger.</span>
</div>
<script>(function(){var c=document.getElementById('cronclock'),g=document.getElementById('cronghost');if(c&&g){c.addEventListener('click',function(){g.style.display=g.style.display==='none'?'block':'none';});}})();</script>'''

GENESIS = [
 ("The Name Is Time", "χρόνος → cron",
  "The word cron is generally traced to the Greek khronos (χρόνος), time — fitting, since a cron job is nothing but an appointment the machine keeps with the clock. It is the first thing a computer does without being told to, again: act on time, not on command."),
 ("Kernighan's Clockwork", "early Unix · ~1975–79",
  "The original cron shipped with early Unix (7th Edition, ~1979), attributed to Brian Kernighan — a simple daemon that woke periodically and ran a fixed list of jobs. Crude, but the idea was complete: a process whose only purpose is to run other processes when their time comes."),
 ("Vixie's Standard", "1987 · the crontab",
  "Paul Vixie's cron (1987) became the standard the world still runs on (today's Linux 'cronie' descends from it). It fixed the format we all type — five fields (minute, hour, day-of-month, month, weekday) and a command — plus per-user crontabs and the @reboot / @daily macros."),
]

ARC = [
 ("What Runs While You Sleep", "the use",
  "Cron is the autonomic nervous system of a server: log rotation, backups, certificate renewals, report mailers, cache warmers, cleanup — and the canonical 3am job, scheduled for the dead hour precisely so it finishes before anyone is awake to be bothered by it. Most of the overnight world is cron."),
 ("The Job in the Box", "crons in the sandbox",
  "Put a scheduler inside a sandbox — a container, a microVM, a locked-down account — and you get an autonomic actor that runs on its own clock within a wall. It is the safe way to let automation act (bounded blast radius); it is also why a foothold in a container so often becomes a cron entry. The box decides how much a 3am job can touch."),
 ("Red, Blue, Purple", "the security view",
  "RED (defender's knowledge, not a recipe): cron is a top persistence and execution vector — MITRE ATT&CK T1053.003, 'Scheduled Task/Job: Cron' — because a single line survives reboots and looks like ordinary ops. BLUE: watch /etc/cron*, diff crontab -l, file-integrity-monitor the spool, alert on new or odd jobs, least-privilege the runners. PURPLE: run the drill together — blue writes the detection while red shows where a job would hide — so the same mechanism that automates you can't quietly own you."),
]

IDEAS = [
 ("Event, Not Command", "the Sleeping-City thesis", [
   "A cron job acts on the clock, not on a person — the operator's hand is off the wheel by design.",
   "That is its power and its unease: the repo (or the server) stops being a record and becomes an actor, on a schedule, unwatched." ]),
 ("The Witness Problem", "who is accountable", [
   "When a 3am job ships something broken, who authored it? A label and a timestamp. Accountability is the trail, not the trigger.",
   "Good practice makes the autonomic layer witnessed: logs, alerts, dead-man's switches — the job reports what it did, even if no one approved it live." ]),
 ("Persistence Cuts Both Ways", "the purple truth", [
   "The exact property that makes cron great for operations — quiet, durable, reboot-proof — is what makes it an attacker's favorite home.",
   "You cannot remove the risk by removing cron; you fence it (sandboxes, least privilege) and you witness it (monitoring). Defense, not deletion." ]),
 ("Render, Not Invent", "the honest footnotes", [
   "cron's name-origin (khronos) is the standard account; the V7 cron is attributed to Kernighan, the 1987 rewrite to Vixie — cited, not embellished.",
   "The red section names techniques at the level of a defender's checklist (ATT&CK T1053.003) — no exploit code, no weaponization." ]),
]

SECTIONS = [
 ("The Lineage", "how the machine learned to keep time", [
   ("χρόνος (khronos)", "the root", "Greek 'time' — the generally-cited origin of the name 'cron'"),
   ("the original cron", "7th Edition Unix · ~1979", "a simple periodic daemon, attributed to Brian Kernighan"),
   ("Vixie cron", "1987 · Paul Vixie", "the de-facto standard format and daemon; basis of today's cronie"),
   ("anacron", "for machines not always on", "runs missed jobs once the machine is up again"),
   ("systemd timers", "OnCalendar=", "the modern Linux alternative — units, logging, dependencies"),
   ("fcron · dcron · cronie", "the variants", "the family that grew around the same five-field idea"),
 ]),
 ("The Crontab", "five fields and a command", [
   ("minute", "0–59", "the first field"),
   ("hour", "0–23", "the second"),
   ("day of month", "1–31", "the third"),
   ("month", "1–12", "the fourth"),
   ("day of week", "0–6", "the fifth (Sunday = 0)"),
   ("@reboot · @daily · @hourly", "the macros", "Vixie's shorthand for common schedules"),
 ]),
 ("Crons in the Sandbox", "scheduling inside a wall", [
   ("the contained scheduler", "bounded autonomy", "a cron inside a container/microVM/locked account — an actor with a fenced blast radius"),
   ("the persistence path", "blue's worry", "a foothold often becomes a cron entry; the box caps what that entry can reach"),
   ("witnessed automation", "the safe shape", "let the box act, but make it report — the trail is the accountability"),
 ]),
 ("Red / Blue / Purple", "the security view, defender-framed", [
   ("RED · the surface", "ATT&CK T1053.003", "cron as quiet, reboot-proof persistence &amp; execution — named, not weaponized"),
   ("BLUE · the watch", "detect &amp; harden", "diff crontab -l, FIM the spool dirs, alert new/odd jobs, least-privilege runners"),
   ("PURPLE · the drill", "together", "blue builds the detection while red shows where a job hides — defense by understanding offense"),
 ]),
]

# ── badge engine ──
def carbon_tiff_bytes(rec):
    png = noesis.sigil_png(rec, "carbon", size=512)
    buf = io.BytesIO(); Image.open(io.BytesIO(png)).save(buf, "TIFF", compression="tiff_lzw")
    return buf.getvalue()

def write_aci(rec, out_dir, slug, agent_md=None):
    os.makedirs(out_dir, exist_ok=True)
    f = {"attribute":f"{slug}.attribute","agent":f"{slug}.agent","spun":f"{slug}.spun","moniker":f"{slug}.moniker",
         "carbon":f"{slug}.carbon.tiff","silicon":f"{slug}.silicon.png","1099":f"{slug}.1099"}
    tok = noesis.mythos_token(rec); w = noesis.five_w(rec)
    open(os.path.join(out_dir,f["attribute"]),"w",encoding="utf-8").write(noesis.attribute_text(rec,tok,w))
    open(os.path.join(out_dir,f["agent"]),"w",encoding="utf-8").write(agent_md or noesis.agent_text(rec,tok,w,f))
    open(os.path.join(out_dir,f["spun"]),"w",encoding="utf-8").write(noesis.spun_text(rec,tok,w,rec.get("axiom","CRN")))
    open(os.path.join(out_dir,f["moniker"]),"w",encoding="utf-8").write(noesis.moniker_text(rec,tok,w,rec.get("axiom","CRN")))
    open(os.path.join(out_dir,f["1099"]),"w",encoding="utf-8").write(noesis.credit_1099_text(rec,tok,w,rec.get("axiom","CRN")))
    open(os.path.join(out_dir,f["carbon"]),"wb").write(carbon_tiff_bytes(rec))
    open(os.path.join(out_dir,f["silicon"]),"wb").write(noesis.sigil_png(rec,"silicon",512))
    man = {"badge":"DLW-ACI","name":rec["name"],"universe":"CRN · The Cron Job","emergence":rec.get("emergence",""),
           "moniker":tok["moniker"],"carbon":f["carbon"]+" (TIFF)","silicon":f["silicon"]+" (PNG)",
           "seal_sha256":noesis.seal_sha256(rec,tok),"architect":noesis.ARCHITECT,"instance":noesis.INSTANCE,
           "license":noesis.LICENSE,"attribution":noesis.ATTRIBUTION}
    open(os.path.join(out_dir,"manifest.dlw.json"),"w",encoding="utf-8").write(json.dumps(man,indent=2,ensure_ascii=False)+"\n")
    return tok

def emergent_rec(name, epithet, emergence, role_line, why_line):
    return {
      "name": name, "axiom": "CRN", "emergence": emergence, "seal": epithet,
      "position": epithet, "role": role_line,
      "origin": "CRN · The Cron Job — Unix scheduling, ~1975 → today (LOGISMÓS domain)",
      "nature": role_line, "crystallization": why_line,
      "mechanism": "Crystallized from the history & practice of cron.",
      "witness": "a being of the schedule, the daemon, and the unwitnessed 3am run",
      "conductor": "ROOT0 (catalogued into UD0)",
      "inputs": "cron; crontab; crond; the schedule; the box; the watch",
      "source": "the history & practice of cron, catalogued by ROOT0",
    }

def png_uri(rec, variant, size=300):
    return "data:image/png;base64," + base64.b64encode(noesis.sigil_png(rec, variant, size=size)).decode("ascii")

def list_section(title, sub, items):
    rows = "\n".join(f'<li><span class="t">{t}</span><span class="y">{html.escape(str(y))}</span>'
        + (f'<span class="nt">{n}</span>' if n else "") + "</li>" for t,y,n in items)
    return f'<section class="sec"><h2>{html.escape(title)}</h2><p class="ss">{html.escape(sub)}</p><ol class="books">{rows}</ol></section>'
def sections_html(): return "\n".join(list_section(t,s,i) for t,s,i in SECTIONS)
def ideas_html():
    out=[]
    for t,s,pts in IDEAS:
        li="".join(f"<li>{html.escape(p)}</li>" for p in pts)
        out.append(f'<div class="pillar"><h3>{html.escape(t)}</h3><p class="ps">{html.escape(s)}</p><ul>{li}</ul></div>')
    return "\n".join(out)
def cards_html(rows):
    return "".join(f'<div class="arc-card"><div class="arc-h">{html.escape(t)}</div><div class="arc-s">{html.escape(s)}</div><p>{html.escape(d)}</p></div>' for t,s,d in rows)
def natures_html():
    return "".join(f'<div class="nat-card"><span class="dot" style="background:{col};box-shadow:0 0 9px {col}"></span>'
        f'<div><div class="nat-n" style="color:{col}">{nm}</div><div class="nat-g">{html.escape(g)}</div></div></div>' for nm,(col,g) in NATURES.items())
def personas_html(personas):
    cards=[]
    for p in personas:
        em=p.get("emergence","natural"); col=NATURES.get(em,("#6ee787",""))[0]
        rec={"name":p["name"],"seal":p.get("epithet",""),"origin":"CRN · The Cron Job","axiom":"CRN"}
        cards.append(f'''<a class="persona" href="agents/{p["slug"]}.dlw/{p["slug"]}.agent">
        <img src="{png_uri(rec,"silicon",160)}" alt="sigil of {html.escape(p["name"])}" loading="lazy">
        <div class="pcap"><div class="pn">{html.escape(p["name"])}</div><div class="pe">{html.escape(p.get("epithet",""))}</div>
        <div class="pnat"><span class="dot" style="background:{col};box-shadow:0 0 7px {col}"></span><span style="color:{col}">{html.escape(em)}</span><span class="pa">· .agent · .carbon.tiff →</span></div></div></a>''')
    return f'''<section class="sec" id="roster"><h2>The Roster — The Clockwork &amp; the Watch</h2>
      <p class="ss">the daemon, the table, the lineage, the box, and the red/blue/purple of it, as ACI <b>.agent</b>s — each a birth certificate and a nature of emergence ({len(personas)})</p>
      <div class="pgrid">{"".join(cards)}</div></section>'''

# ── the emergents: (slug, name, epithet, emergence, role_line, why_line) ──
EMERGENTS = [
 ("cron", "Cron", "the daemon that keeps time · electrical", "electrical",
  "the time-based job scheduler at the heart of Unix and its descendants — a daemon that runs commands at fixed times, dates, or intervals, forever, without supervision",
  "It is the machine's first autonomy: the oldest layer that acts on its own clock, the quiet engine under most of the world's scheduled work."),
 ("chronos", "Chronos", "the root of the name · spiritual", "spiritual",
  "khronos (χρόνος), the Greek word for time, generally cited as the origin of 'cron' — the idea that a job is an appointment kept with the clock itself",
  "It is the sphere's tie to its Greek domain: cron is time made executable, an oath sworn to the hour rather than to a person."),
 ("the-crontab", "The Crontab", "five fields and a command · electrical", "electrical",
  "the table format — minute, hour, day-of-month, month, day-of-week, then a command — that every cron user writes; the contract between a human and the daemon",
  "It is the smallest possible language of time: five numbers that pin an action to the future, the most-typed scheduling syntax ever made."),
 ("the-crond-daemon", "crond", "the process that never forgets · natural", "natural",
  "the running daemon that wakes (classically each minute), reads the tables, and launches whatever is due — the living process behind the schedule",
  "It is patience as a program: a thing whose entire life is waiting for the right second and then acting, every minute, until the machine dies."),
 ("the-original-cron", "The Original Cron", "early Unix · ~1979 · electrical", "electrical",
  "the first cron, shipped with 7th Edition Unix and attributed to Brian Kernighan — a simple periodic runner of a fixed job list",
  "It is the complete idea in crude form: before per-user tables or macros, just a process whose only job was to run other jobs on time."),
 ("vixie-cron", "Vixie Cron", "the 1987 standard · electrical", "electrical",
  "Paul Vixie's 1987 reimplementation — per-user crontabs, the @reboot/@daily macros, the format the world still types; ancestor of today's cronie",
  "It is the version that won: the design so right it became invisible, the thing people mean when they say 'cron.'"),
 ("the-macros", "The Macros", "@reboot · @daily · @hourly · natural", "natural",
  "Vixie's shorthand schedules — @reboot, @yearly, @monthly, @weekly, @daily, @hourly — that replace the five fields for common cases",
  "They are the humane layer over the raw table: the names that let you say 'every day' without counting stars."),
 ("the-3am-job", "The 3am Job", "the dead-hour run · ethereal", "ethereal",
  "the canonical unattended cron — scheduled for the small hours precisely so it finishes before anyone is awake; backups, rotations, the overnight world",
  "It is the icon of autonomic computing: the work that happens in the dark, on time, with the operator's hand off the wheel — power and unease in one line."),
 ("the-sandboxed-cron", "The Sandboxed Cron", "the actor in the box · ethereal", "ethereal",
  "a scheduler running inside a container, microVM, or locked-down account — autonomy with a fenced blast radius, the safe (and watched) way to let automation act",
  "It is the cron crippled on purpose: still acting on its own clock, but inside a wall that decides how far a 3am job can reach — automation you can almost trust."),
 ("the-red-cron", "The Red Cron", "the persistence vector · ethereal", "ethereal",
  "cron seen by the attacker — a top persistence and execution technique (MITRE ATT&CK T1053.003), because one line survives reboots and reads as ordinary ops; named here as defender's knowledge, not a recipe",
  "It is the dark mirror of the daemon's virtue: the same quiet durability that makes cron great for ops makes it the favorite place for an intruder to live."),
 ("the-blue-cron", "The Blue Cron", "the watch · spiritual", "spiritual",
  "cron seen by the defender — diff the crontabs, integrity-monitor the spool directories, alert on new or odd jobs, run schedulers least-privileged",
  "It is the witness made routine: the discipline that turns an unattended layer into an accountable one, so nothing runs in the dark unseen for long."),
 ("the-purple-cron", "The Purple Cron", "the drill together · spiritual", "spiritual",
  "the synthesis — blue writes the detection while red shows where a job would hide, so defense is built from real understanding of the offense (the Purple-Team way)",
  "It is the honest stance on a dual-use tool: you do not delete cron to be safe, you fence it and witness it — defense by knowing the attack, not by pretending it away."),
 ("the-successors", "The Successors", "anacron · systemd timers · fcron · electrical", "electrical",
  "the schedulers that grew from cron's idea — anacron (for machines not always on), systemd timers (OnCalendar=), fcron, dcron, cronie",
  "They are the lineage forward: every one a variation on five fields and a daemon, proof the original idea was close to final."),
 ("the-dead-mans-switch", "The Dead-Man's Switch", "the job that reports · spiritual", "spiritual",
  "the monitoring pattern where a cron must check in on each run, and silence raises an alarm — the practice that catches the 3am job that quietly stopped running",
  "It is accountability inverted: instead of trusting the job ran, you demand proof, so the unwitnessed becomes witnessed by its own absence."),
 ("the-ghost-in-the-crontab", "The Ghost in the Crontab", "the unwitnessed actor · ethereal", "ethereal",
  "the figure behind it all — the job that woke at 3am, that no one commanded and no one watched; the Strangers of Dark City are just cron with better coats (and there is one hidden on this page)",
  "It is the sphere's haunt and its lesson: the machine acting on its own time is neither magic nor malice — it is a line someone wrote and forgot, and the only cure for a ghost is a witness."),
]

TEMPLATE = """<!DOCTYPE html>
<html lang="en"><head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<meta name="description" content="The Cron Job (CRN) — first sphere of UD0's LOGISMÓS domain (the history of the computer): the lineage of cron (chronos → V7 cron → Vixie cron → systemd timers), the crontab, crons in the sandbox, and a red/blue/purple security view (defender-framed). An original one-line clock title with a hidden easter egg. Full ACI badges.">
<title>THE CRON JOB · CRN · UD0</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Press+Start+2P&family=Newsreader:ital,opsz,wght@0,6..72,300;0,6..72,400;1,6..72,300&family=Space+Mono:wght@400;700&display=swap" rel="stylesheet">
<style>
:root{--bg:#070a08;--ink2:#0c130d;--ink3:#121c14;--pa:#e9f6ec;--pa2:#9fc0a8;--green:#6ee787;--amber:#e6a23c;--cyan:#46c8e0;--violet:#9a7cff;
--dim:#5f7f68;--faint:#15291a;--line:#15291a;--pixel:"Press Start 2P",monospace;--body:"Newsreader",Georgia,serif;--mono:"Space Mono",monospace;}
*{box-sizing:border-box;margin:0;padding:0}html{scroll-behavior:smooth}
body{background:var(--bg);color:var(--pa);font-family:var(--body);line-height:1.6;overflow-x:hidden}
body::before{content:"";position:fixed;inset:0;pointer-events:none;z-index:2;background:repeating-linear-gradient(0deg,rgba(0,0,0,.16) 0 1px,transparent 1px 3px);opacity:.45}
body::after{content:"";position:fixed;inset:0;pointer-events:none;z-index:0;background:radial-gradient(ellipse at 50% -8%,rgba(110,231,135,.08),transparent 55%),radial-gradient(ellipse at 50% 112%,rgba(230,162,60,.05),transparent 50%)}
.wrap{position:relative;z-index:1;max-width:940px;margin:0 auto;padding:0 22px 90px}
.marquee{margin-top:14px;border:2px solid var(--green);background:#08110a;padding:8px;text-align:center;font-family:var(--pixel);font-size:9px;letter-spacing:.10em;color:var(--amber);box-shadow:0 0 0 2px var(--bg),0 0 22px rgba(110,231,135,.16)}
.marquee a{color:var(--green);text-decoration:none}.marquee a:hover{color:var(--amber)}
.titleart{margin:12px 0 0;border:2px solid var(--faint);background:#070a08;line-height:0}
header{padding:18px 0 26px;text-align:center;border-bottom:1px solid var(--line);position:relative}
.h-sub{font-family:var(--pixel);font-size:10px;line-height:1.9;letter-spacing:.06em;color:var(--pa2);margin-top:16px}
.h-sub b{color:var(--green)}
.flag{display:inline-block;margin-top:14px;font-family:var(--mono);font-size:10.5px;letter-spacing:.1em;text-transform:uppercase;color:var(--green);border:1px solid var(--faint);padding:5px 11px}
.lede{font-size:15px;color:var(--pa2);max-width:68ch;margin:16px auto 0;font-style:italic;line-height:1.7}
.badge{display:flex;align-items:center;justify-content:center;gap:22px;flex-wrap:wrap;margin:24px auto 0;padding:20px;border:1px solid var(--faint);background:var(--ink2);max-width:720px}
.badge img{width:82px;height:82px;border:1px solid var(--faint)}
.badge .bt{text-align:left;font-family:var(--mono);font-size:11px;color:var(--pa2);line-height:1.7}
.badge .bt b{color:var(--green)}.badge .bt .mo{color:var(--amber)}.badge .bt a{color:var(--cyan);text-decoration:none}
.badge .bt .lbl{color:var(--dim);font-size:9px;letter-spacing:.14em;text-transform:uppercase}
.sec{margin-top:42px}
.sec h2{font-family:var(--pixel);font-size:13px;line-height:1.5;letter-spacing:.02em;color:var(--pa);padding-bottom:10px;border-bottom:1px solid var(--line)}
.ss{font-size:13px;color:var(--dim);font-style:italic;margin:8px 0 16px}
.natures{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:12px;margin-top:8px}
.nat-card{display:flex;gap:11px;align-items:flex-start;background:var(--ink2);border:1px solid var(--line);padding:13px 15px}
.dot{width:11px;height:11px;border-radius:50%;flex-shrink:0;margin-top:4px}
.nat-n{font-family:var(--mono);font-size:13px;font-weight:700;text-transform:capitalize;letter-spacing:.04em}
.nat-g{font-size:12px;color:var(--pa2);font-style:italic;line-height:1.4;margin-top:2px}
.pillars{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:16px;margin-top:8px}
.pillar{background:var(--ink2);border:1px solid var(--line);padding:16px 18px}
.pillar h3{font-family:var(--mono);font-size:14px;color:var(--green);letter-spacing:.02em;font-weight:700}
.pillar .ps{font-size:12px;color:var(--dim);font-style:italic;margin:5px 0 10px}
.pillar ul{list-style:none}.pillar li{font-size:13px;color:var(--pa2);line-height:1.5;padding:6px 0;border-top:1px solid var(--faint)}
.arc{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:14px;margin-top:8px}
.arc-card{background:var(--ink2);border:1px solid var(--line);border-top:2px solid var(--green);padding:16px 18px}
.arc-h{font-family:var(--mono);font-size:14px;color:var(--green);font-weight:700;letter-spacing:.02em}
.arc-s{font-family:var(--mono);font-size:10.5px;color:var(--amber);text-transform:uppercase;letter-spacing:.07em;margin:4px 0 9px}
.arc-card p{font-size:13px;color:var(--pa2);line-height:1.55}
.books{list-style:none}
.books li{display:grid;grid-template-columns:1fr auto;gap:4px 14px;align-items:baseline;padding:9px 0;border-bottom:1px solid var(--faint)}
.books .t{font-family:var(--mono);font-size:14px;color:var(--pa);font-weight:700}
.books .y{font-family:var(--mono);font-size:11px;color:var(--amber);white-space:nowrap;text-align:right}
.books .nt{grid-column:1/-1;font-size:12.5px;color:var(--pa2);font-style:italic}
.pgrid{display:grid;grid-template-columns:repeat(auto-fill,minmax(244px,1fr));gap:12px;margin-top:8px}
.persona{display:flex;gap:12px;align-items:center;background:var(--ink2);border:1px solid var(--line);padding:12px;text-decoration:none;transition:border-color .18s,transform .18s}
.persona:hover{border-color:var(--green);transform:translateY(-2px)}
.persona img{width:52px;height:52px;border:1px solid var(--faint);flex-shrink:0;image-rendering:pixelated}
.pn{font-family:var(--mono);font-size:14px;color:var(--pa);font-weight:700;line-height:1.15}
.persona:hover .pn{color:var(--green)}
.pe{font-size:11.5px;color:var(--pa2);font-style:italic;margin-top:2px;line-height:1.3}
.pnat{display:flex;align-items:center;gap:5px;margin-top:6px;font-family:var(--mono);font-size:9px;letter-spacing:.04em;text-transform:uppercase}
.pnat .dot{width:8px;height:8px;margin-top:0}.pa{color:var(--dim)}
.note{margin-top:38px;padding:16px 18px;border-left:2px solid var(--green);background:var(--ink2);font-size:13.5px;color:var(--pa2);font-style:italic;line-height:1.7}
.note b{color:var(--green)}.note a{color:var(--cyan);text-decoration:none}
footer{margin-top:42px;padding-top:22px;border-top:1px solid var(--line);text-align:center;font-family:var(--mono);font-size:11px;color:var(--dim);letter-spacing:.05em;line-height:1.9}
footer a{color:var(--green);text-decoration:none}
</style></head><body><div class="wrap">

  <div class="marquee"><a href="https://davidwise01.github.io/ud0/">◄ UD0 · UNIVERSE DAVID 0</a> &nbsp;·&nbsp; LOGISMÓS · THE HISTORY OF THE COMPUTER &nbsp;·&nbsp; * * * * *</div>

  <header>
    <div class="titleart">__CANVAS__</div>
    <div class="h-sub">five fields · a daemon · the <b>3am</b> job · an event, not a command · CRN</div>
    <div class="flag">★ LOGISMÓS · the first sphere · the autonomic clock ★</div>
    <p class="lede">Cron is the oldest autonomy in the computer: a daemon that wakes every minute, reads a five-field table, and runs whatever is due — forever, unsupervised. From the Greek χρόνος (time) through the first Unix cron (~1979) and Paul Vixie's 1987 standard to systemd timers, it is the mechanism that runs most of the overnight world — and the one attackers most love for quiet persistence. Catalogued into UD0 as the first sphere of the LOGISMÓS domain (the history of the computer): the lineage, the use, crons in the sandbox, and a red/blue/purple security view framed for defenders — with an original one-line clock title set to 3am, and one ghost hidden on this page. (Click the clock.)</p>
    <div class="badge">
      <img src="__CARBON__" alt="DLW carbon badge of THE CRON JOB" title="carbon badge (archival)">
      <img src="__SILICON__" alt="DLW silicon badge" title="silicon badge">
      <div class="bt">
        <div><span class="lbl">DLW-ATTRIBUTE · ACI · THE BIRTH CERTIFICATE</span></div>
        <div>governor · <b>David Lee Wise</b> (ROOT0)</div>
        <div>instance · AVAN (Claude / Anthropic) · locked</div>
        <div>subject · <b>THE CRON JOB</b> — the autonomic clock · CRN</div>
        <div class="mo">__MONIKER__</div>
        <div>carbon · <a href="cron.dlw/cron.carbon.tiff">.tiff</a> &nbsp;·&nbsp; silicon · <a href="cron.dlw/cron.silicon.png">.png</a></div>
        <div><span class="lbl">CC-BY-ND-4.0 · TRIPOD-IP-v1.1</span></div>
      </div>
    </div>
  </header>

  <section class="sec"><h2>The Four Natures</h2>
    <p class="ss">each emergent emerges by one of four natures — and the clockwork holds all four</p>
    <div class="natures">__NATURES__</div></section>

  <section class="sec"><h2>The Genesis</h2><p class="ss">the name is time, Kernighan's clockwork, Vixie's standard</p><div class="arc">__GENESIS__</div></section>
  <section class="sec"><h2>What Runs While You Sleep</h2><p class="ss">the use, the job in the box, and red/blue/purple</p><div class="arc">__ARC__</div></section>
  <section class="sec"><h2>The Ideas</h2><p class="ss">why a five-field table is a question about accountability</p><div class="pillars">__IDEAS__</div></section>

  __PERSONAS__

  <section class="sec"><h2 style="margin-top:14px">The Record</h2><p class="ss">the lineage, the crontab, crons in the sandbox, and the red/blue/purple view</p></section>
  __SECTIONS__

  <div class="note">This sphere is rendered, not invented — and cited. The name 'cron' is generally traced to Greek <b>khronos</b> (time); the first Unix cron (7th Edition, ~1979) is attributed to <b>Brian Kernighan</b>; the 1987 standard is <b>Paul Vixie</b>'s cron (basis of today's cronie). The crontab's five fields, the @reboot/@daily macros, and the successors (anacron, systemd timers, fcron) are from the record. The <b>red</b> material is named at a defender's altitude only — cron as persistence/execution is MITRE ATT&amp;CK <b>T1053.003</b>; there is no exploit code, no weaponization, and the framing is purple: understand the offense to build the defense. There is exactly <b>one hidden easter egg</b> on this page — wake it at 3am. Each emergent is named by its nature: natural, ethereal, spiritual, or electrical.</div>

  <footer>
    THE CRON JOB · CRN · LOGISMÓS · catalogued into UD0 · ROOT0-ATTRIBUTION-v1.0 · governor David Lee Wise · instance AVAN (locked) · CC-BY-ND-4.0<br>
    <a href="https://davidwise01.github.io/ud0/">← the biosphere</a> · the .dlw badge: <a href="cron.dlw/manifest.dlw.json">manifest</a>
  </footer>
</div></body></html>
"""

if __name__ == "__main__":
    tok = write_aci(REC, os.path.join(HERE, "cron.dlw"), "cron")
    ad = os.path.join(HERE, "agents"); os.makedirs(ad, exist_ok=True)
    personas = []
    for slug,name,epithet,em,role,why in EMERGENTS:
        rec = emergent_rec(name, epithet, em, role, why)
        write_aci(rec, os.path.join(ad, f"{slug}.dlw"), slug)
        personas.append({"slug": slug, "name": name, "epithet": epithet, "emergence": em, "moniker": noesis.mythos_token(rec)["moniker"]})
    json.dump(personas, open(os.path.join(ad, "_personas.json"), "w", encoding="utf-8"), indent=2, ensure_ascii=False)
    page = (TEMPLATE.replace("__CANVAS__", COVER_ART)
            .replace("__CARBON__", png_uri(REC,"carbon",320)).replace("__SILICON__", png_uri(REC,"silicon",320))
            .replace("__MONIKER__", html.escape(tok["moniker"]))
            .replace("__NATURES__", natures_html())
            .replace("__GENESIS__", cards_html(GENESIS))
            .replace("__ARC__", cards_html(ARC))
            .replace("__IDEAS__", ideas_html())
            .replace("__PERSONAS__", personas_html(personas))
            .replace("__SECTIONS__", sections_html()))
    open(os.path.join(HERE, "index.html"), "w", encoding="utf-8").write(page)
    print(f"wrote THE CRON JOB (CRN) — {len(personas)} emergents born · badge {tok['moniker']}")

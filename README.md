# ICN T1 Parking Monitor

Checks the official Incheon Airport website every 10 minutes and sends the
following T1 parking availability to ntfy:

- P1 long-term parking
- P1 parking tower (east)
- P2 long-term parking
- P2 parking tower (west)

The workflow sends updates around 3, 13, 23, 33, 43, and 53 minutes past the
hour during these windows:

- 2026-09-23 from now until 20:00 KST (test window)
- 2026-09-24 from 08:00 until 10:00 KST

It pauses between the windows and disables itself at **2026-09-24 10:00 KST**.

Subscribe to this topic in the ntfy app:

`icn-parking-e7c05cfe-d92d-445c-8916-c49b767b749f`

You can also run the workflow immediately from the repository's Actions tab
using **Run workflow**.

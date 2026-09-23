# ICN T1 Parking Monitor

Checks the official Incheon Airport website every 10 minutes and sends the
following T1 parking availability to ntfy:

- P1 long-term parking
- P1 parking tower (east)
- P2 long-term parking
- P2 parking tower (west)

The one-time cloud workflow sends updates every 10 minutes during these windows:

- 2026-09-23 from now until 22:00 KST (test window)
- 2026-09-24 from 07:21 until 08:00 KST (early-start extension)
- 2026-09-24 from 08:00 until 10:00 KST

It waits in chained GitHub-hosted jobs between the windows and finishes at
**2026-09-24 10:00 KST**. It does not depend on a local computer or Codex.

Subscribe to this topic in the ntfy app:

`icn-parking-e7c05cfe-d92d-445c-8916-c49b767b749f`

You can also run the workflow immediately from the repository's Actions tab
using **Run workflow**.

# Candidate identity

Use the bundled `scripts/candidate.py` when a Git working tree, including dirty changes, needs a reproducible identity. Pass an explicit review base, then reuse the returned full base commit on later runs. The script prints JSON and does not stage, commit, write a snapshot, or create Git objects.

The v1 fingerprint is SHA-256 of length-prefixed fields: schema marker, resolved base commit, HEAD commit, raw NUL-delimited Git index entries, then sorted unique tracked/non-ignored untracked paths. Each path contributes its name, file type/executable marker, and SHA-256 content digest; symlinks contribute their target, missing tracked paths a deletion marker. File timestamps do not contribute. Git index entries include staged content identities, modes, and conflict stages. Different staging can conservatively invalidate evidence even if working contents match.

Run it before and after checks or review and compare schema, base, and fingerprint. Identity includes the resolved HEAD and index; a commit changes it. For commit/rebase equivalence, compare actual content and base rather than claiming the old fingerprint equals the new one.

## Limits

- This is a non-atomic observation, not an immutable snapshot. Concurrent edits that change and revert during inspection can evade before/after comparison. Use a stable isolated view for stronger guarantees.
- Ignored files, external services, dependencies outside Git, environment variables, runtime configuration, and tool versions are outside the digest. Record relevant environment evidence separately. If ignored inputs affect behavior, identify them separately without publishing secrets or use an appropriate snapshot.
- Submodules are rejected, including clean ones, because their nested inputs require recursive capture. Unsupported file types and unreadable inputs also fail instead of yielding a partial fingerprint.
- Raw working bytes and platform file modes can differ across operating systems or checkouts. Compare within the same environment; do not promise cross-platform digest equality.
- Unborn repositories lack a HEAD commit and cannot use this helper. Use another explicit content manifest and disclose its coverage.
- Printing or saving the JSON inside the reviewed tree creates another input and changes identity. Keep transient evidence in the response, Engram, or outside the tree.

The same helper is bundled in verify and rdd so either skill can be installed independently. Keep the two copies byte-identical. An equivalent implementation can follow this contract; Python is optional for the skill itself.

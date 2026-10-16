# Repository rename record

The existing `DayenaJeong/cohe-artifact` repository was renamed in place to `DayenaJeong/cohe` on 2026-10-16 after author approval. Canonical documentation URLs use the new name; the old repository and release URLs redirect to it. Repository identity, scientific tag and release assets were preserved.

`mint-lab/cohe` is the separate project-homepage repository. Its URL, ownership and GitHub Pages deployment are not part of this rename.

## Preserve the scientific release

- Existing repository ID: `1229820373`.
- Reviewed main commit: `54c201bb79800cedcfd4842b8f5fbc652555da3e`.
- Fixed tag: `v1.0-neurips2026`.
- Annotated tag object: `e69471c1dc0237843fa46cc3aab89058c7b57843`.
- Tagged scientific commit: `01b7d54050d1458d8a0f15f3b2c07c95b52a5f3f`.
- Existing release ID: `402478271`, with 13 assets: nine checkpoint archives and four manifests/notes files.

The rename updated the existing repository's name through the GitHub repository API, equivalent to **Settings → General → Repository name → Rename**. No replacement repository was created, Git history copied, release retagged, or release asset edited. The scientific tag remains fixed; README/asset edits belong to main's documentation history.

[GitHub's rename documentation](https://docs.github.com/en/repositories/creating-and-managing-repositories/renaming-a-repository) describes redirects and recommends updating local remotes. Do not reuse the old repository name for another repository, because that would remove its redirects.

The repository ID, tag object, tagged commit, release ID and asset digests were checked unchanged after the rename. Future maintenance should preserve these identities and test both the canonical release URL and the old redirect.

## Local remote and commit identity

Update other existing local checkouts to the canonical URL with:

```bash
git remote set-url origin https://github.com/DayenaJeong/cohe.git
git remote -v
```

The approved documentation change uses the DayenaJeong account. The existing history verifies this account's numeric-ID noreply email. Repository-local identity settings are:

```bash
git config --local user.name "DayenaJeong"
git config --local user.email "114856982+DayenaJeong@users.noreply.github.com"
git var GIT_AUTHOR_IDENT
git var GIT_COMMITTER_IDENT
```

Use authenticated DayenaJeong credentials for pushes of this documentation change. Do not add other authors or co-author trailers. These settings are local to this checkout.

## Canonical documentation URLs prepared

| File | Prepared update |
| --- | --- |
| `README.md` | Code/checkpoint links and fixed-release links use the new canonical repository URL. |
| `CITATION.cff` | `repository-code` and software `url` use the new repository; the paper citation links to the official NeurIPS presentation record. |
| `docs/FAQ.md` | Checkpoint-release link. |
| `docs/RELEASE_RECORD.md` | Release link only; version and scientific commit stay unchanged. |
| `checkpoints/README.md` | Release link only; all coverage and loading information stays unchanged. |
| `experiments/ddpm_ordering/README.md` | Release link only. |
| `experiments/imagenet1k_vae_gate3/README.md` | Release link only. |

Historical references in `archive/release_process/PAPER_UPDATE_REPORT.md:50` and `archive/release_process/validation.md:5,8` remain unchanged as records of the original release. Their old links should redirect after the rename. Scientific CSV/JSON manifests, arrays, code and checkpoints are not rewritten.

## External references requiring separate follow-up

| Location | Existing reference / action |
| --- | --- |
| `mint-lab/cohe`, `src/data/results.ts:3` | The `artifact` constant still uses `https://github.com/DayenaJeong/cohe-artifact`. A separately authorized update should change it to the new URL. It also generates the release link and commit-pinned evidence links; preserve the pinned scientific commit. |
| `mint-lab/cohe`, `README.md:3` | Update the artifact repository URL separately. |
| Published homepage, `https://mint-lab.github.io/cohe/` | Code, checkpoints, reporting guide, seed-record and evidence links currently derive from the old artifact URL. Update and redeploy the separate site only when authorized; the homepage URL itself stays unchanged. |
| Camera-ready manuscript, Appendix artifact-scope paragraph | The existing project/release discussion cites the old repository URL. Its redirect can preserve access; any manuscript URL edit is a separate task. |
| Fixed release notes, downloaded archives and historical copies | Keep the scientific release unchanged. Do not replace historical metadata just to remove an old spelling. |
| Third-party citations, bookmarks and local clones | They cannot be enumerated exhaustively from this repository. Use GitHub redirects, and update owned references/local remotes when discovered. |

The official paper link stays `https://neurips.cc/virtual/2026/poster/139659`; the project homepage stays `https://mint-lab.github.io/cohe/`. No DOI, arXiv identifier or unverified PDF URL is introduced.

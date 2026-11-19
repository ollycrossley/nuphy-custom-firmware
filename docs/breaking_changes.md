# Breaking Changes

This document describes QMK's Breaking Change process. A Breaking Change is any change which modifies how QMK behaves in a way that in incompatible or potentially dangerous. We limit these changes so that users can have confidence that updating their QMK tree will not break their keymaps.

This also includes any keyboard moves within the repository.

The breaking change period is when we will merge PRs that change QMK in dangerous or unexpected ways. There is a built-in period of testing so we are confident that any problems caused are rare or unable to be predicted.

Practically, this means QMK merges the `develop` branch into the `master` branch on a 3-month cadence.

## What has been included in past Breaking Changes?

* [2024 May 26](ChangeLog/20240526)
* [2024 Feb 25](ChangeLog/20240225)
* [2023 Nov 26](ChangeLog/20231126)
* [Older Breaking Changes](breaking_changes_history)

## When is the next Breaking Change?

The next Breaking Change is scheduled for August 25, 2024.

### Important Dates

* 2024 May 26 - `develop` is tagged with a new release version. Each push to `master` is subsequently merged to `develop` by GitHub actions.
* 2024 Jul 28 - `develop` closed to new PRs.
* 2024 Jul 28 - Call for testers.
* 2024 Aug 4 - Last day for merges -- after this point `develop` is locked for testing and accepts only bugfixes
* 2024 Aug 18 - `develop` is locked, only critical bugfix PRs merged.
* 2024 Aug 22 - `master` is locked, no PRs merged.
* 2024 Aug 25 - Merge `develop` to `master`.
* 2024 Aug 25 - `master` is unlocked. PRs can be merged again.

## What changes will be included?

To see a list of breaking changes merge candidates you can look at the [`core` label](https://github.com/qmk/qmk_firmware/pulls?q=is%3Aopen+label%3Acore+is%3Apr). This label is applied whenever a PR is raised or changed, but only if the PR includes changes to core areas of QMK Firmware. A PR with that label applied is not guaranteed to be merged in the current cycle. New changes might be added between now and when `develop` is closed, and it is generally the responsibility of the submitter to handle conflicts. There is also another label used by QMK Collaborators -- `breaking_change_YYYYqN` -- which signifies to maintainers that it is a strong candidate for inclusion, and should be prioritized for review.

If you want your breaking change to be included in this round you need to create a PR and have it accepted by QMK Collaborators before `develop` closes. After `develop` closes, new submissions will be deferred to the next breaking changes cycle.

The simpler your PR is, the easier it is for maintainers to review, thus a higher likelihood of a faster merge. Large PRs tend to require a lot of attention, refactoring, and back-and-forth with subsequent reviews -- with other PRs getting merged in the meantime larger unmerged PRs are far more likely to be susceptible to conflicts.

Criteria for acceptance:

* The PR is complete and ready to merge
* GitHub checks for the PR are green whenever possible
    * A "red" check may be disregarded by maintainers if the items flagged are unrelated to the change proposed in the PR
        * Modifications to existing files should not need to add license headers to pass lint, for instance.
        * If it's not directly related to your PR's functionality, prefer avoiding making a change.

Strongly suggested:

* The PR has a ChangeLog file describing the changes under `<qmk_firmware>/docs/Changelog/20240526`.
    * This should be in Markdown format, with a name in the format `PR12345.md`, substituting the digits for your PRs ID.
    * One strong recommendation that the ChangeLog document matches the PR description on GitHub, so as to ensure traceability.

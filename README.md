# pantsbuild Sample Repo

This repo was created to provide a sample environment for testing out supporting
[Trunk Merge Queue](https://docs.trunk.io/merge-queue)
[Parallel Mode](https://docs.trunk.io/merge-queue/parallel-queues) on
[Pants](https://www.pantsbuild.org/) powered repos. In order to use Parallel Mode, the list of
dependencies that a created PR affects needs to be
[sent to Merge Queue](https://docs.trunk.io/merge-queue/parallel-queues/api) - this repo shows how
to do that

## Repo Dependency Layout

This repo contains the following Pants targets:

- is_number
  - dependent on nothing
- is_even
  - dependent on `is_number`
- is_odd
  - dependent on `is_number`
- is_even_or_odd
  - dependent on `is_odd` and `is_even`
  - transitively dependent on `is_number`
- main
  - dependent on `is_even_or_odd`
  - transitively dependent on `is_odd`, `is_even`, and `is_number`

In the pants world, you can run `pants dependents --transitive`
([reference link](https://www.pantsbuild.org/2.21/docs/using-pants/project-introspection#dependents---find-which-targets-depend-on-a-target))
to see pants output the specific targets that each module is dependant on

## Calculating Impacted Targets

In order to determine what pants targets a PR you create specifically changes, pants must compare
your current PR's branch against the branch that Trunk Merge Queue would be merging the PR into.
Pants makes this easy with the `--changed-since` argument
([reference link](https://www.pantsbuild.org/2.21/docs/using-pants/advanced-target-selection#running-over-changed-files-with---changed-since))
as it understands git.

Knowing this, you can generate a list of impacted targets to send to Merge Queue with the following
command assuming you currently have the PR's branch checked out:

`pants --changed-since=origin/${MERGE_INSTANCE_BRANCH} --changed-dependents=transitive dependents --transitive`

Broken down:

- `--changed-since=origin/${MERGE_INSTANCE_BRANCH}` will make Pants only consider targets that have
  changed directly between the current PR and the branch Merge Queue will merge the PR into
- `--changed-dependents=transitive` will also make Pants include the targets that are dependant on
  the directly changed targets above
- `dependents --transitive` must be specified since Pants needs to be told a goal. This will make it
  list out all targets and their dependents that were changed as a result of the PR.

This command will return a new-line delimited list than can then be
[sent directly to Trunk](https://docs.trunk.io/merge-queue/parallel-queues/api)

## Testing Pants On This Repo

In order to test all of this out, all you need to do is run `./get-pants.sh` - after that, the
command `pants` should be available in your path. If you already have Pants installed, this step can
be skipped

## Running Tests

There are some sanity tests in this repo - to run them, you can either use `python -m unittest` or
`pants test ::` to get Pants to do it

# demo-immutable-infrastructure

step 1: show current prod application page

step 2: make changes to application

step 3: push to master, create a release tag

step 4: jenkins to bake new release AMI

step 5: jenkins to deploy new release AMI to staging

step 6: show staging application page (functional/load testing)

step 7: jenkins to deploy new release AMI to production

step 8: show production application page (blue - green)

step 9: delete the staging stack, and old production stack
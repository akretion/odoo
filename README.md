# Odoo OCA repository

This projet is a prebuild of odoo core part. The goal is to speed up the build of the source code in odoo repository

## To update this code:

1. Update **spec.yml** 

2. Start the build:

     `docker-compose -f etc/docker/docker-compose.yml -p odoo_oca up`

3. Rename the branch **merged** with the name of the issue jira and subject: 

    `git branch -m 'merged' 'M2-****_fixsomething'`
    `git push origin 'M2-****_fixsomething'`

4. Test the branch by updating locally the branch in spec.yml of /odoo repository
5. Merge the branch on master and deploy it in production.

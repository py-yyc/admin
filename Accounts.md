## Meetup

http://www.meetup.com/py-yyc/

Uses RBAC, so there’s no master password.

There can only be one organizer, and the organizer has to pay a
subscription fee to remain organizer. The subscription fee is not
refundable or transferable if there’s a change in organizers; the new
organizer has to pay for their own subscription.

## Assembly CS

Not really an account, but we have the “4th Wednesday of every month”
slot at [Assembly CS](http://www.assemblycs.com). See the contact info
[here](secrets/assembly.gpg).

## Trello

https://trello.com/pyyyc

Uses RBAC, so there’s no master password.

People can be invited to individual boards, such as the [PyYYC
Talks](https://trello.com/b/OkwBY2BT/pyyyc-talks) one, without being added
to the team.

Go to https://trello.com/pyyyc/members to add someone to the team, giving
them access to all boards.

## github.com/py-yyc

https://github.com/py-yyc

Uses RBAC, so there’s no master password. Owners can add people at
https://github.com/orgs/py-yyc/people

If you are an Owner of the organization, please set your organization
membership to “Public” at https://github.com/orgs/py-yyc/people so that
people can find you.

## pyyyc.org

The website is currently a static site, served as a checkout of:

https://github.com/py-yyc/py-yyc.github.com

There is a cronjob that syncs from github every five minutes, so just
commit to the repo to update the website. Cronjob errors go to
organizers@pyyyc.org; you can check https://pyyyc.org/last-sync to see if
the cronjob is still working.

It would be pretty straightforward to configure the current host to run a
Django site instead.

This domain is registered and hosted at DreamHost, under Andrew’s account.
Carson also has access to administer the domain and unix user in the
dreamhost panel, allowing the domain to be transferred.

## Twitter

[@PyYYC](https://twitter.com/pyyyc)

Using [TweetDeck](https://tweetdeck.twitter.com), you can share access to
this account without sharing the password.

The password is in `secrets/twitter.gpg`.

## Slides.com

https://slides.com/pyyyc

The password is in `secrets/slides.gpg`.

## Slack

Andrew has registered a free Slack account at pyyyc.slack.com. If people
start using it, he will share admin access. YYC Design might be better, as
it’s a more general Calgary-wide slack for technology.

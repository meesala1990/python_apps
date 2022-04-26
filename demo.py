from jira import JIRA 
jiraOptions = {'server':'https://jira.gfs.com/'}
jira = JIRA(options = jiraOptions, basic_auth = ("sandeep","Samsung@0790"))
for singleIssue in jira.search_issues(jql_str='project in (TS, DUS, NATC) AND status = "Ready for Release"'):print('{}: {}:{}'.format(singleIssue.key, singleIssue.fields.summary,singleIssue.fields.reporter.displayName))
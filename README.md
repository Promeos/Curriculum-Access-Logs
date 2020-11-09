![Time Series Project Header](./visuals/log-exploration.png)

## Goals
Use 3 years of curriculum access data to determine the following:

1. Which lesson appears to attract the most traffic consistently across cohorts (per program)?
2. Is there a cohort that referred to a lesson significantly more that other cohorts seemed to gloss over? 
3. Are there students who, when active, hardly access the curriculum? If so, what information do you have about these students? 
4. Is there any suspicious activity, such as users/machines/etc accessing the curriculum who shouldn’t be? Does it appear that any web-scraping is happening? Are there any suspicious IP addresses? Any odd user-agents? 
5. At some point in the last year, ability for students and alumni to cross-access curriculum (web dev to ds, ds to web dev) should have been shut off. Do you see any evidence of that happening? Did it happen before? 
6. What topics are grads continuing to reference after graduation and into their jobs (for each program)? 
7. Which lessons are least accessed? 
8. Anything else I should be aware of?


### Deliverables
<strong>Your Team Lead will present this. Convey information in a detailed and clear manner.</strong>
1. Compose an email with answers to your Team Lead's questions. Present relevant findings.
> Include a link to your notebook in GitHub
> Attach Executive Summary slide
2. GitHub notebook
> Format the notebook as a Q&A between you and your Team Lead. Ask and answer the questions with documentation to backup your analysis.
> Note to self: Clean your graphs!
3. Excutive Summary: One Slide
> Note to self: Use Canva.

---
## Executive Summary
[In Progress]


## Data Dictionary
| Feature | Description | datatype |
| :------ | :---------- | :------- |
| `datetime` | Index of the dataset. The date and time a page was viewed by a user | DatetimeIndex |
| `page_viewed` | The content the user accessed | object |
| `user_id` | The user who accessed the curriculum | int64 |
| `cohort_id` | The cohort the user is assigned to | int 64 |
| `ip` | The ip address the user is using to access the curriculum | object |

## Data Science Pipeline
---
### Acquisition
[In Progress]

### Preparation
[In Progress]

### Exploration
[In Progress]

### Conclusion
[In Progress]

## Acknowledgements
---
[Codeup](https://codeup.com/)

Codeup Data Science Instructors

Darden Cohort
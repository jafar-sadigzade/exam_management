# Exam Scoring Rules
## Scoring rules in ExamModel models
### Example
```json
{
  "scoring_rules": [
    {
      "subject_name": "Azərbaycan dili",
      "question_count": 20,
      "points_per_correct": 7,
      "points_per_incorrect": -1.75
    },
    {
      "subject_name": "Riyaziyyat",
      "question_count": 25,
      "points_per_correct": 7,
      "points_per_incorrect": -1.75
    },
    {
      "subject_name": "İngilis dili",
      "question_count": 35,
      "points_per_correct": 7,
      "points_per_incorrect": -1.75
    },
    {
      "subject_name": "Tarix",
      "question_count": 10,
      "points_per_correct": 7,
      "points_per_incorrect": -1.75
    },
    {
      "subject_name": "Təbiət",
      "question_count": 10,
      "points_per_correct": 7,
      "points_per_incorrect": -1.75
    }
  ],
  "total_score_calculation": "sum"
}
```
## Correct answer in Exam models
### Example
```json
{
  "subjects": [
    {
      "subject_name": "Azərbaycan dili",
      "correct_answers": "BDCCADBACDBACDDBACAA"
    },
    {
      "subject_name": "Riyaziyyat",
      "correct_answers": "BABADDBDACACCDBC*CBDCACDA"
    },
    {
      "subject_name": "İngilis dili",
      "correct_answers": "BADACDCACBCDDAABCBADCAADABBCCBDABCD"
    },
    {
      "subject_name": "Tarix",
      "correct_answers": "CDCABBCDCA"
    },
    {
      "subject_name": "Təbiət",
      "correct_answers": "BCDCBBDACD"
    }
  ]
}
```
## Answers in Student model
### Example
```json
[
    {
        "subject_name": "Azərbaycan dili",
        "student_answers": "BACABDBBCDBAADDBACAA",
        "correct_answers": "BDCCADBACDBACDDBACAA"
    },
    {
        "subject_name": "Riyaziyyat",
        "student_answers": "BABADDAD A C D CAAB CABCA",
        "correct_answers": "BABADDBDACACCDBC*CBDCACDA"
    },
    {
        "subject_name": "İngilis dili",
        "student_answers": "BCDACBCAABCDACAB CADCABDCBDBDBDABBB",
        "correct_answers": "BADACDCACBCDDAABCBADCAADABBCCBDABCD"
    },
    {
        "subject_name": "Tarix",
        "student_answers": "CDAAAB DCB",
        "correct_answers": "CDCABBCDCA"
    },
    {
        "subject_name": "Təbiət",
        "student_answers": "BCDCBBDCDD",
        "correct_answers": "BCDCBBDACD"
    }
]
```
## Results in Student model
### Example
```json
{
    "subject_scores": {
        "Azərbaycan dili": {
            "right_answers": 15,
            "wrong_answers": 5,
            "total": 96.25
        },
        "Riyaziyyat": {
            "right_answers": 15,
            "wrong_answers": 5,
            "total": 96.25
        },
        "İngilis dili": {
            "right_answers": 21,
            "wrong_answers": 13,
            "total": 124.25
        },
        "Tarix": {
            "right_answers": 6,
            "wrong_answers": 3,
            "total": 36.75
        },
        "Təbiət": {
            "right_answers": 8,
            "wrong_answers": 2,
            "total": 52.5
        }
    },
    "total_score": 406.0
}
```
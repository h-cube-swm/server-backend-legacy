# JSON 응답 딕셔너리를 모아둔 코드
APIOnly = {"success": True, "status": 200, "comment": "API Only"}
postOnly = {"success": False, "status": 400, "comment": "only POST allowed"}

ok = {"success": True, "status": 200, "comment": "OK"}
no = {"success": False, "status": 400, "comment": "NO"}

illegalArgument = {"success": False, "status": 400, "comment": "Illegal Argument"}

# Survey 관련
invalidSurveyID = {"success": False, "status": 400, "comment": "Invalid Survey ID"}
surveyCannotEdit = {
    "success": False,
    "status": 400,
    "comment": "Survey Cannot Edit(Survey Status is not Editing)",
}
modifySurveySucceed = {
    "success": True,
    "status": 200,
    "comment": "Modify Survey Succeed",
}

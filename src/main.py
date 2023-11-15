from fine_tuning.fine_tuning import fine_tuning_execute
import openai

if __name__ == "__main__":
    job_id = "ftjob-MrZhIIPGrWiQ4gEktbVb8Jrw"
    result = openai.FineTuningJob.retrieve(job_id)
    print(result)

import { FileUp, Send } from "lucide-react";
import { useState, useRef } from "react";
import { createPortal } from "react-dom";
import { useScoreResumeMutation } from "./__generated__/types";
import { TailSpin } from "react-loader-spinner";
import EvaluationModal from "./EvaluationModal";

interface FormData {
  job: string;
  resume: File | null;
}

export default function App() {
  const fileUploadRef = useRef<HTMLInputElement | null>(null);
  const [formData, setFormData] = useState<FormData>({
    job: "",
    resume: null,
  });
  const [formErrors, setFormErrors] = useState<Record<string, string>>({});
  const [loading, setLoading] = useState(false);
  const [responseError, setResponseError] = useState<any>(null);
  const [showModal, setShowModal] = useState(false);
  const [scoreResume] = useScoreResumeMutation();

  const handleJobChange = (event: React.ChangeEvent<HTMLTextAreaElement>) => {
    setFormData({
      ...formData,
      job: event.target.value,
    });
  };

  const handleResumeUpload = (event: React.ChangeEvent<HTMLInputElement>) => {
    const resume = event.target.files?.[0];
    setFormData({
      ...formData,
      resume: resume ?? null,
    });
  };

  const resetFormData = () => {
    setFormData({ job: "", resume: null });
    if (fileUploadRef.current) {
      fileUploadRef.current.value = "";
    }
  };

  const validateForm = () => {
    let errors: Record<string, string> = {};

    if (formData.job.length === 0) {
      errors.job = "You must provide a job description!";
    }
    if (!formData.resume) {
      errors.resume = "You must provide a resume!";
    }

    setFormErrors(errors);
    return errors;
  };

  const handleSubmit = async (event: React.MouseEvent<HTMLButtonElement>) => {
    event.preventDefault();

    const errors = validateForm();
    if (Object.keys(errors).length !== 0) {
      console.log(formData.job.length === 0);
      return;
    }

    try {
      setLoading(true);
      const { data } = await scoreResume({
        variables: {
          file: formData.resume,
          job: formData.job,
        },
      });
      console.log(data);
      resetFormData();
      setShowModal(true);
    } catch (error) {
      console.log(error);
      setResponseError(error);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="container flex flex-col items-center gap-6 py-12">
      <div className="text-center">
        <h1 className="text-4xl font-semibold">Resume Scanner</h1>
        <p>Evaluate how well your resume fits a job description.</p>
      </div>
      <form className="flex flex-col gap-3 w-5/6 p-8 rounded-lg bg-zinc-800">
        <div>
          <label htmlFor="job" className="block mb-1 font-semibold text-2xl">
            Job Description
          </label>
          <textarea
            name="job"
            id="job"
            placeholder="Enter a job description..."
            className="w-full border-solid min-h-96 text-black p-1 rounded-sm bg-gray-100"
            onChange={handleJobChange}
            value={formData.job}
          />
          {formErrors.job && (
            <span className="text-red-500">{formErrors.job}</span>
          )}
        </div>

        <div>
          <div className="flex items-center mb-1">
            <label
              htmlFor="resume"
              className="px-6 py-3 border-gray-300 border-2 hover:cursor-pointer rounded-md align-middle inline-flex gap-2 items-center"
            >
              <FileUp className="inline-block" /> Upload Resume (PDF)
            </label>
            <span className="ml-2">
              {formData.resume?.name ?? "No file selected"}
            </span>
            <input
              ref={fileUploadRef}
              type="file"
              id="resume"
              name="resume"
              accept=".pdf"
              className="hidden"
              onChange={handleResumeUpload}
            />
          </div>
          {formErrors.resume && (
            <span className="text-red-500">{formErrors.resume}</span>
          )}
        </div>

        <div>
          <button
            className="px-6 py-3 text-white bg-blue-600 hover:cursor-pointer rounded-md align-middle inline-flex gap-2 items-center"
            onClick={handleSubmit}
          >
            {loading ? (
              <TailSpin
                visible={true}
                height="20"
                width="20"
                color="white"
                ariaLabel="tail-spin-loading"
                radius="1"
                wrapperStyle={{}}
                strokeWidth={5}
                wrapperClass="mr-1 text-bold"
              />
            ) : (
              <Send className="inline-block" />
            )}
            Submit
          </button>
        </div>
        {createPortal(
          <EvaluationModal onClose={() => setShowModal(false)} />,
          document.getElementById("modal-root")!
        )}
      </form>
    </div>
  );
}

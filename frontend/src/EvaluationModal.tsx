interface EvaluationModalProps {
  onClose: () => void;
}

export default function EvaluationModal({ onClose }: EvaluationModalProps) {
  return (
    <div className="fixed top-0 left-0 w-screen h-screen bg-black/50 flex items-center justify-center z-50">
      <div className="bg-white min-w-[800px] w-1/2 h-3/4 rounded-md p-6">
        <h1 className="text-black text-2xl font-semibold">Resume Evaluation</h1>
      </div>
    </div>
  );
}

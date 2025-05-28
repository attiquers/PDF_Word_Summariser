import React, { useState } from "react";

interface UploadBoxProps {
  addFiles: (files: File[]) => void;
  files: File[];
  uploadedFiles: string[];
}

const UploadBox: React.FC<UploadBoxProps> = ({ addFiles, files, uploadedFiles }) => {
  const [dragging, setDragging] = useState(false);

  const handleDragOver = (e: React.DragEvent<HTMLDivElement>) => {
    e.preventDefault();
    setDragging(true);
  };

  const handleDragLeave = (e: React.DragEvent<HTMLDivElement>) => {
    e.preventDefault();
    setDragging(false);
  };

  const handleDrop = (e: React.DragEvent<HTMLDivElement>) => {
    e.preventDefault();
    setDragging(false);

    const droppedFiles = Array.from(e.dataTransfer.files).filter(
      (file) => file.type === "application/pdf"
    );
    if (droppedFiles.length > 0) {
      addFiles(droppedFiles);
    } else {
      alert("Only PDF files are supported.");
    }
  };

  const handleFileInputChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const selectedFiles = Array.from(e.target.files || []).filter(
      (file) => file.type === "application/pdf"
    );
    if (selectedFiles.length > 0) {
      addFiles(selectedFiles);
    }
  };

  return (
    <div
      onDragOver={handleDragOver}
      onDragLeave={handleDragLeave}
      onDrop={handleDrop}
      className={`border-2 border-dashed rounded-lg p-8 text-center flex flex-col items-center space-y-4 transition-colors duration-300
        ${dragging ? "bg-blue-200 border-blue-400" : "border-gray-400 bg-white"}`}
      style={{ cursor: "pointer" }}
    >
      <div className="text-5xl">📄</div>

      <label
        htmlFor="file-upload"
        className="cursor-pointer inline-block px-6 py-2 bg-blue-600 text-white rounded hover:bg-blue-700"
      >
        Choose Files
      </label>
      <input
        id="file-upload"
        type="file"
        accept=".pdf"
        multiple
        onChange={handleFileInputChange}
        className="hidden"
      />

      <p className="text-sm text-gray-500">or drop files here</p>

      {files.length > 0 && (
        <div className="mt-4 w-full max-h-48 overflow-y-auto text-sm text-gray-700">
          <p className="font-semibold mb-2">Selected Files:</p>
          <ul className="space-y-1">
            {files.map((file, index) => (
              <li
                key={index}
                className="flex justify-between text-xs border-b border-gray-200 pb-1"
              >
                <span className="truncate max-w-xs">{file.name}</span>
                <span className="text-gray-500">
                  {(file.size / 1024).toFixed(2)} KB
                </span>
                {uploadedFiles.includes(file.name) && (
                  <span className="text-green-600 font-bold ml-2">✔</span>
                )}
              </li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
};

export default UploadBox;

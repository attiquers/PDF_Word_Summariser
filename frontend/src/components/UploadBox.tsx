import React from "react";

interface Props {
  addFiles: (files: File[]) => void;
  files: File[];
  uploadedFiles: string[];
}

const UploadBox: React.FC<Props> = ({ addFiles, files, uploadedFiles }) => {
  const handleDrop = (e: React.DragEvent<HTMLDivElement>) => {
    e.preventDefault();
    const dropped = Array.from(e.dataTransfer.files).filter(f => f.type === "application/pdf");
    addFiles(dropped);
  };

  const handleFileInputChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const selected = Array.from(e.target.files || []).filter(f => f.type === "application/pdf");
    addFiles(selected);
    e.target.value = "";
  };

  return (
    <div
      onDragOver={e => e.preventDefault()}
      onDrop={handleDrop}
      className="border-2 border-dashed p-6 rounded bg-white shadow"
    >
      <div className="text-3xl mb-2">📄</div>
      <label
        htmlFor="file-input"
        className="cursor-pointer bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700"
      >
        Select PDF Files
      </label>
      <input
        id="file-input"
        type="file"
        accept=".pdf"
        multiple
        onChange={handleFileInputChange}
        className="hidden"
      />
      <p className="mt-2 text-sm text-gray-600">Or drag and drop PDF files here</p>

      {files.length > 0 && (
        <ul className="mt-4 space-y-1 text-sm">
          {files.map((file, idx) => (
            <li key={idx} className="flex justify-between items-center">
              <span>{file.name}</span>
              {uploadedFiles.includes(file.name) && (
                <span className="text-green-500 ml-2">✅</span>
              )}
            </li>
          ))}
        </ul>
      )}
    </div>
  );
};

export default UploadBox;

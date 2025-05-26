import React, { useState } from "react";
import UploadBox from "./components/UploadBox";

const App: React.FC = () => {
  const [files, setFiles] = useState<File[]>([]);
  const [uploaded, setUploaded] = useState<string[]>([]);
  const [dirHandle, setDirHandle] = useState<any>(null);
  const addFiles = (newFiles: File[]) => {
    const names = new Set(files.map(f => f.name));
    const unique = newFiles.filter(f => !names.has(f.name));
    setFiles(prev => [...prev, ...unique]);
  };

  const chooseDirectory = async () => {
    try {
      // Ask user to choose target folder
      const handle = await (window as any).showDirectoryPicker();
      setDirHandle(handle);
      alert("Folder selected!");
    } catch (err) {
      alert("Directory access was denied.");
    }
  };

  const uploadFiles = async () => {
    if (!dirHandle) return alert("Please choose a folder first.");

    for (const file of files) {
      if (uploaded.includes(file.name)) continue;

      try {
        const fileHandle = await dirHandle.getFileHandle(file.name, { create: true });
        const writable = await fileHandle.createWritable();
        await writable.write(file);
        await writable.close();
        setUploaded(prev => [...prev, file.name]);
      } catch (err) {
        console.error(`Failed to write ${file.name}:`, err);
      }
    }
  };

  return (
    <div className="p-6 bg-gray-100 min-h-screen text-gray-900">
      <h1 className="text-2xl font-bold mb-4">📂 Upload PDFs to Local Folder</h1>

      <UploadBox addFiles={addFiles} files={files} uploadedFiles={uploaded} />

      <div className="mt-4 flex space-x-4">
        <button
          onClick={chooseDirectory}
          className="bg-purple-600 text-white px-4 py-2 rounded hover:bg-purple-700"
        >
          Choose Target Folder
        </button>
        <button
          onClick={uploadFiles}
          className="bg-green-600 text-white px-4 py-2 rounded hover:bg-green-700"
        >
          Upload Files
        </button>
      </div>
    </div>
  );
};

export default App;

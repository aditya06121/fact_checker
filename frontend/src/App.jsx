import React from "react";

function App() {
  return (
    <div className="flex flex-col items-center justify-center min-h-screen bg-gray-100 dark:bg-gray-900 text-gray-800 dark:text-gray-200">
      <h1 className="text-4xl font-extrabold mb-4 text-blue-600 dark:text-sky-400">
        Fact Checker Application
      </h1>
      <p className="text-lg text-center max-w-2xl mb-6">
        Welcome to the Fact Checker application! This tool will help you verify
        the authenticity of articles by categorizing them on a scale of 1 to 5:
        Trusted News, Satire, Hoax, Propaganda, and more. Additionally, it will
        use a web crawler to locate the original article for you.
      </p>
      <p className="text-md text-center max-w-xl italic text-red-500">
        Note: The user interface will not be available until at least the web
        crawler is completed.
      </p>
    </div>
  );
}

export default App;

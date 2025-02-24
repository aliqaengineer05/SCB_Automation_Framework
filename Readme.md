# Mobile Automation Testing Framework

This project is a mobile automation testing framework using **Robot Framework**, **Appium**, and **Python**. It is designed to perform automated tests on mobile applications following a modular structure with **Page Object Model (POM)** and reusable keywords. It also integrates **Allure Reports** for better test result reporting.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Setup Guide](#setup-guide)
- [Folder Structure](#folder-structure)
- [Running Tests](#running-tests)
- [CI Integration](#ci-integration)
- [Test Reports](#test-reports)
- [Priority & Severity Annotations](#priority-severity-annotations)
- [Conclusion](#conclusion)

## Prerequisites

Before you can use this automation framework, ensure you have the following software installed:

1. **Python** (version 3.7 or above)
   - Download and install Python from [python.org](https://www.python.org/).
   
2. **Appium** (version 2.x or above)
   - Install Appium globally via npm:
     ```bash
     npm install -g appium
     ```
   - Ensure **Node.js** is installed, which you can download from [nodejs.org](https://nodejs.org/).

3. **Java Development Kit (JDK)** (version 13 or above)
   - Download and install JDK from [Oracle](https://www.oracle.com/java/technologies/javase-jdk13-downloads.html).
   - Set the `JAVA_HOME` and update `PATH`:
     ```bash
     export JAVA_HOME=/path/to/your/jdk
     export PATH=$JAVA_HOME/bin:$PATH
     ```

4. **Android Studio** (version 4.x or above)
   - Download and install Android Studio from [developer.android.com](https://developer.android.com/studio).
   - Set up an Android Emulator or connect a real Android device.
   - Set the `ANDROID_HOME` environment variable:
     ```bash
     export ANDROID_HOME=/path/to/your/android/sdk
     export PATH=$ANDROID_HOME/tools:$ANDROID_HOME/platform-tools:$PATH
     ```

5. **PyCharm** (IDE recommended for managing the project)
   - Download from [JetBrains](https://www.jetbrains.com/pycharm/).

6. **Allure Framework** (for test reporting)
   - Install Allure Commandline using Homebrew (macOS):
     ```bash
     brew install allure
     ```
   - For Windows/Linux, follow the installation steps on [Allure’s GitHub](https://github.com/allure-framework/allure2).

## Setup Guide

Follow the steps below to set up the framework:

### 1. Install Python
- Download and install Python 3.7 or above from [python.org](https://www.python.org/).
- Add Python to the system `PATH` during installation.

### 2. Install Appium
Install Appium globally using npm:
```bash
npm install -g appium

### **3. Install Java Development Kit (JDK)**
- Download and install JDK from Oracle.
- Set up JAVA_HOME and update PATH as shown in the Prerequisites section.

### 4. Install Android Studio
- Download and install Android Studio from developer.android.com.
- Set the ANDROID_HOME environment variable as shown in the Prerequisites section.

### 5. Install Python Libraries
Install the required Python libraries by running:

```pip install -r requirements.txt

### 6. Set Up Robot Framework
- Install Robot Framework and AppiumLibrary:
```pip install robotframework
```pip install robotframework-appiumlibrary

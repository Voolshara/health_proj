<template>
  <div class="container-form">
    <Dialog />
    <p class="main-par">Анкета 1</p>
    <p class="sub_information" style="font-size: 20px">
      С вами на связи всегда будет личный помощник (ваш личный врач). Задавайте
      ему любые вопросы, поручайте дела и просто общайтесь в любое удобное для
      вас время/ мы с вами 24/7. Заполнение каждой анкеты действительно до 3х
      дней.
    </p>
    <el-divider />

    <div v-if="form_is_send" class="form-send">Форма отправлена</div>
    <div v-else>
      <el-upload
        class="avatar-uploader"
        action="http://localhost:5000/upload_avatar"
        :show-file-list="false"
        :on-success="handleAvatarSuccess"
        :before-upload="beforeAvatarUpload"
      >
        <img v-if="imageUrl" :src="imageUrl" class="avatar" />
        <el-icon v-else class="avatar-uploader-icon"><Plus /></el-icon>
      </el-upload>
      <p>Вам необходимо отправить нам фото 6x5;</p>

      <el-form
        :model="form"
        label-width="300px"
        class="form"
        :label-position="'top'"
      >
        <el-form-item label="Ваш рост (см)">
          <el-input-number
            v-model="form.growth"
            :controls="false"
            placeholder="Укажите число в см"
            size="large"
          />
        </el-form-item>

        <el-form-item label="Ваш вес (кг)">
          <el-input-number
            v-model="form.weight"
            :controls="false"
            placeholder="Укажите число в см"
            size="large"
          />
        </el-form-item>

        <el-form-item label="Ваш город">
          <el-input v-model="form.city" placeholder="Укажите город" />
        </el-form-item>

        <el-form-item label="Имеется ли у вас сопутствующие заболевания?">
          <el-radio-group v-model="form.is_illy">
            <el-radio :label="true" size="large" border>Да</el-radio>
            <el-radio :label="false" size="large" border>Нет</el-radio>
          </el-radio-group>
        </el-form-item>

        <el-form-item label="Принимаете ли вы лекарства?">
          <el-radio-group v-model="form.is_use_treatments">
            <el-radio :label="true" size="large" border>Да</el-radio>
            <el-radio :label="false" size="large" border>Нет</el-radio>
          </el-radio-group>
        </el-form-item>

        <el-form-item label="Владеете ли вы какой-либо информацией о инсульте?">
          <el-radio-group v-model="form.know_some_information">
            <el-radio :label="true" size="large" border>Да</el-radio>
            <el-radio :label="false" size="large" border>Нет</el-radio>
          </el-radio-group>
        </el-form-item>

        <el-form-item label="Была ли у вас реабилитация?">
          <el-radio-group v-model="form.reabilitation">
            <el-radio :label="true" size="large" border>Да</el-radio>
            <el-radio :label="false" size="large" border>Нет</el-radio>
          </el-radio-group>
        </el-form-item>

        <el-form-item>
          <el-button type="primary" @click="onSubmit"
            >Отправить запрос на восстановление</el-button
          >
        </el-form-item>
      </el-form>
    </div>
  </div>
</template>

<script>
import Dialog from "@/components/dialog.vue";
export default {
  name: "FormFirst",
  components: {
    Dialog,
  },
  data() {
    return {
      imageUrl: "/img/file_add.png",
      form: {
        growth: "",
        weight: "",
        city: "",
        is_illy: "",
        is_use_treatments: "",
        know_some_information: "",
        reabilitation: "",
        form_is_send: false,
      },
    };
  },
  methods: {
    onSubmit: function () {
      // fetch("http://localhost:5600/form1", {
      fetch("http://localhost:5600/form1", {
        method: "POST", // *GET, POST, PUT, DELETE, etc.
        mode: "cors", // no-cors, *cors, same-origin
        cache: "no-cache", // *default, no-cache, reload, force-cache, only-if-cached
        credentials: "same-origin", // include, *same-origin, omit
        headers: {
          "Content-Type": "application/json",
          "Access-Control-Allow-Private-Network": true,
        },
        redirect: "follow", // manual, *follow, error
        referrerPolicy: "no-referrer", // no-referrer, *no-referrer-when-downgrade, origin, origin-when-cross-origin, same-origin, strict-origin, strict-origin-when-cross-origin, unsafe-url
        body: JSON.stringify({
          data: this.form,
        }), // body data type must match "Content-Type" header
      })
        .then((response) => response.json())
        .then((data) => {
          (this.form_is_send = true), console.log(data);
        })
        .catch((error) => {
          console.error("Error:", error);
          return null;
        });
    },
  },
};
</script>

<style scoped>
.avatar-uploader .avatar {
  width: 178px;
  height: 178px;
  display: block;
}
</style>

<style>
.avatar-uploader .el-upload {
  border: 1px dashed var(--el-border-color);
  border-radius: 6px;
  cursor: pointer;
  position: relative;
  overflow: hidden;
  transition: var(--el-transition-duration-fast);
}

.avatar-uploader .el-upload:hover {
  border-color: var(--el-color-primary);
}

.el-icon.avatar-uploader-icon {
  font-size: 28px;
  color: #8c939d;
  width: 178px;
  height: 178px;
  text-align: center;
}
.container-form {
  align-items: center;
  text-align: center;
}

.sub_information {
  width: 70vw;
  margin: auto;
  margin-bottom: 15px;
}

.form {
  position: relative;
  align-self: center;
  padding: 0 3vw 0 0;
  width: 40vw;
  margin: auto;
  margin-top: 50px;
}

.main-par {
  color: #0836b5;
  background-image: url("@/assets/bg_header.png");
  font-style: normal;
  font-weight: 900;
  font-size: 70px;
  line-height: 145px;
}
</style>
